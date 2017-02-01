'''
From: http://dtmoodie.blogspot.cz/2015/02/getting-image-watch-like-debugging-in.html
'''

import gdb
import cv2
import sys
import numpy


class PlotterCommand(gdb.Command):
    def __init__(self):
        super(PlotterCommand, self).__init__("plot",
                                             gdb.COMMAND_DATA,
                                             gdb.COMPLETE_SYMBOL)
    def invoke(self, arg, from_tty):
        args = gdb.string_to_argv(arg)
      
      
        # generally, we type "plot someimage" in the GDB commandline
        # where "someimage" is an instance of cv::Mat
        v = gdb.parse_and_eval(args[0])
      
        # the value v is a gdb.Value object of C++
        # code's cv::Mat, we need to translate to
        # a python object under cv2.cv
        image_size =  (v['cols'],v['rows'])
        # print v
        # these two below lines do not work. I don't know why
        # channel = gdb.execute("call "+ args[0] + ".channels()", False, True)
        # channel = v.channels();
        CV_8U  = 0
        CV_8S  = 1
        CV_16U = 2
        CV_16S = 3
        CV_32S = 4
        CV_32F = 5
        CV_64F = 6
        CV_USRTYPE1=7
        CV_CN_MAX = 512
        CV_CN_SHIFT = 3
        CV_MAT_CN_MASK = (CV_CN_MAX - 1) << CV_CN_SHIFT
        flags = v['flags']
        channel = (((flags) & CV_MAT_CN_MASK) >> CV_CN_SHIFT) + 1
        CV_DEPTH_MAX = (1 << CV_CN_SHIFT)
        CV_MAT_DEPTH_MASK = CV_DEPTH_MAX - 1
        depth = (flags) & CV_MAT_DEPTH_MASK
        IPL_DEPTH_SIGN = 0x80000000
        cv_elem_size = (((4<<28)|0x8442211) >> depth*4) & 15
        if (depth == CV_8S or depth == CV_16S or depth == CV_32S):
                mask = IPL_DEPTH_SIGN
        else:
                mask = 0
        ipl_depth = cv_elem_size*8 | mask   

      
        # conver the v['data'] type to "char*" type
        char_type = gdb.lookup_type("char")
        char_pointer_type =char_type.pointer()
        buffer = v['data'].cast(char_pointer_type)
        
        #data_address = unicode(v['data']).encode('utf-8').split()[0]
        #data_address = int(data_address, 16)
        #buffer = data_address
        #print("data_address:", buffer)

      
        # read bytes from inferior's memory, because
        # we run the opencv-python module in GDB's own process
        # otherwise, we use memory corss processes       

        print("Rows:", int(v['rows']))
        buf = v['step']['buf']
        print("buf:", int(buf[0]), int(buf[1]))
        bytes = buf[0] * v['rows'] # buf[0] is the step? Not quite sure.
        print("bytes:", int(bytes))

        line_step = v['step']['p'][0]
        print("line_step:", int(line_step))

        print('Reading image')

        inferior = gdb.selected_inferior()
        mem = inferior.read_memory(buffer, bytes)
        print('Read successful')

        if(depth == CV_8U):
            print('8bit image')
            img = numpy.frombuffer(mem, count=bytes, dtype=numpy.uint8)
        if(depth == CV_16U):
            print('16bit image')
            img = numpy.frombuffer(mem, count=bytes, dtype=numpy.uint16)
        if(depth == CV_32F):
            print('32bit float image')
            img = numpy.frombuffer(mem, count=bytes, dtype=numpy.float32)
            print("From buffer done")
        img = img.reshape((v['rows'], v['cols'], channel))
        print(img.shape)
        # create a window, and show the image

        cv2.imshow("debugger", img)
      
        # the below statement is necessory, otherwise, the Window
        # will hang
        cv2.waitKey(0)
PlotterCommand()

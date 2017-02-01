'''
Heavily based on: https://github.com/dtmoodie/GDB-ImageWatch/blob/master/qt-imageWatch/cvTypes.py
'''

from dumper import *

CV_MAT_DEPTH_TO_STR = {0: 'CV_8U',
                       1: 'CV_8S',
                       2: 'CV_16U',
                       3: 'CV_16S',
                       4: 'CV_32S',
                       5: 'CV_32F',
                       6: 'CV_64F'}

#def qform__cv__Mat():
#    return "Normal,Displayed"

def qform__cv__Mat():
    return [SeparateFormat]

def qdump__cv__Mat(d, value):
    cols = value["cols"]
    rows = value["rows"]
    
    #d.putValue('{} x {}'.format(rows, cols))#, CV_MAT_DEPTH_TO_STR[depth], channels))

    flags = value["flags"]
    depth = int(flags) & 7
    channels = 1 + (int(flags) >> 3) & 63
    #line_step = value['step']['p'][0]

    cv_mat_format = "{}x{} {}C{}"

    # depending if you want to be Pythonic, use int() or other class, or
    # use Value.interer() or other data type method from Dumper API
    d.putValue(cv_mat_format.format(int(rows), cols.integer(), CV_MAT_DEPTH_TO_STR[depth], channels))

    dims = value['dims']
    members = value.members(False)
    #print('members:', members)
    print("Printing members")

    #for member in members:
    #    print("Name:", member.name)

    #line_step = value['step']['p'][0]
    #data_start = value['data']
    ##data_start = d.extractPointer(d.addressOf(value['datatstart']))
    #data_start = value['datastart']
    #data_end = value['dataend']
    #nbytes = data_end - data_start
    #nbytes = rows * cols * channels
    d.putNumChild(4)
    #padding = line_step - cols * channels

    if d.isExpanded():
        with Children(d):
            d.putSubItem('rows', rows)
            d.putSubItem('cols', cols)
            d.putIntItem('channels', channels) # technically, this is not int, but...
            d.putSubItem('dims', dims)
            #p.putSubItem('data_start', data_start)
    
    '''
    bits = gdb.Value(data_start.cast(value['data'].type.pointer()))
    with Children(d):
       d.putSubItem("Data start", data_start)
       d.putSubItem("Rows", rows)
       d.putSubItem("Cols", cols)
       d.putSubItem("Channels", channels)
       d.putSubItem("Depth", depth)
       d.putSubItem("Num Bytes", nbytes)
       d.putSubItem("Data end", data_end)
       d.putSubItem("Row Step", line_step)
       d.putSubItem("Padding", padding)
       with SubItem(d, "data"):
           d.putValue("0x%x" % bits)
           d.putNumChild(0)
           d.putType("void *")
    format = d.currentItemFormat()
    if format == 1:
        d.putDisplay(StopDisplay)
    if format == 2:
        #file = tempfile.mkstemp(prefix="gdbpy_")
        #filename = file[1].replace("\\", "\\\\")
        #gdb.execute("dump binary memory %s %s %s" % (filename, bits, bits + nbytes))
        #d.putDisplay(DisplayImageFile, " %d %d %d %d %s" % (cols, rows, nbytes, channels, filename))
        d.putField("editformat", DisplayImageData)
        d.put('editvalue="')
        d.put('%08x%08x%08x%08x' % (cols, rows, nbytes, channels))
        d.put(d.readMemory(bits,nbytes))
        d.put('",')
    '''

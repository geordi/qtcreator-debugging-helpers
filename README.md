# Jan's QtCreator Debugging Helpers
These are my QtCreator Debugging Helpers

I use these debugging helpers to help me debug my stuff in QtCreator (mainly OpenCV programs).
Since September 2016, there're OpenCV debugging helpers, but I'd like to see more info on cv::Mat so I use my own helpers. OpenCV debugging helper almost entirely based on [5].

## Image Watch Like Experience in QtCreator

I was trying to use [8] and other repos that originate in [9], but it didn't work for me. Using just [7], I was able to get a window with image content.

## References

### General QtCreator Debugging Helper Related
[1] [QtCreator Documentation](http://doc.qt.io/qtcreator/creator-debugging-helpers.html)

[2] [Qt Blog: Peek and Poke, Vol. 3](http://blog.qt.io/blog/2010/04/22/peek-and-poke-vol-3/)

[3] [Stackoverflow's: How to write a debugging helper for qtcreator?](http://stackoverflow.com/questions/34354573/how-to-write-a-debugging-helper-for-qtcreator)

[4] [Peter Lohrmann's: Writing Debug Visualizers for GDB / QtCreator 2.8](http://plohrmann.blogspot.cz/2013/10/writing-debug-visualizers-for-gdb.html)

### OpenCV QtCreator Debugging Helper Related
[5] [dtmoodie's CV Types](https://github.com/dtmoodie/GDB-ImageWatch/blob/master/qt-imageWatch/cvTypes.py)

[6] [QT Forum's: Debug helper for visualizing images](https://forum.qt.io/topic/47370/debug-helper-for-visualizing-images)

[7] [Daniel Moodie's: Getting image watch like debugging in Qt Creator](http://dtmoodie.blogspot.cz/2015/02/getting-image-watch-like-debugging-in.html)

[8] [dtmoodie's Image Watch in QtCreator](https://github.com/dtmoodie/GDB-ImageWatch)

[9] [Renato Florentino Garcia's gdb-imshow](https://github.com/renatoGarcia/gdb-imshow)

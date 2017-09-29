# General

```
#!/bin/sh
# This is a comment!
echo Hello World        # This is a comment, too!
```

The first line tells Unix that the file is to be executed by /bin/sh. This is the standard location
of the Bourne shell on just about every Unix system. If you're using GNU/Linux, /bin/sh is normally
a symbolic link to bash (or, more recently, dash).

The first line is *not treated as a comment*. This is a special directive which Unix treats specially. It means that even if you are using csh, ksh, or anything else as your interactive shell, that what follows should be interpreted by the Bourne shell.

You could also use  ```#!/usr/bin/perl``` to tell the shell that the program which follows should be executed by perl.

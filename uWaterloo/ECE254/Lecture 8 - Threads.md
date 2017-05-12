## Threads

A process has three major components: executable program, data created/needed by program,
and execution context of program (files opened, resources allocated, etc).

A process has at least one *thread*, and can have many.

The term "thread" is a short form of *Thread of Execution*. A thread of execution is a
sequence of executable commands that can be scheduled to run on CPU. Threads also have
some state (where in the sequence of exectuable commands the program is) ands stores
some local variables.

A multithreaded program is one that uses more than one thread, at least some of the time.
When a program is started, it begins with an initial thread (where the ```main``` thread
is) and that main thread can create some additional threads if needed.

Note that threads can be created/destroyed within a program dynamically: a thread can
be created to handle a specific background task, like writing changes to the database,
and will terminate when it is done. Or a created thread might be persistent.

In a process w/ multiple threads, each thread has its own:

1. Thread execution state (like process state: running, ready, blocked...)
2. Saved thread context when not running
3. Execution stack
4. Local variables
5. Access to the memory and resources of the process (shared with all threads in that process)

All threads of a process share the state and resources of the process. If one thread opens a file,
other threads in that process can also access that file.

The way programs are now, they're all multithreaded. One common way of dividing the program
into threads is seperate the user interface from a time-consuming action.

For a file-transfer program, if the file upload has started, we could not use the UI if they
share a thread.

## Motivation for Threads

Why choose threads rather than create a new process? Performance.

1. Creating new thread is much faster than making new process
2. Terminating/cleaning up thread is much faster than process
3. Takes less time to switch b/w threads with same process (less data needs to be stored/restored)
4. Threads share same memory space, they don't need to use IPC mechanisms.
5. As in the file transfer program, use of threads allows the program to be responsive even when
a part of the program is blocked

This last advantage, background work, is one of 4 common examples of the uses of threads in a general
purpose operating system.

1. *Foreground and Background Work:* Ability to run something in the background to keep program responsive
2. *Asynchronous Processing:* Protect against power failure or a crash. Write data in main memory to disk
periodically. This can be done as a background task so it does not disrupt the user's workflow.
3. *Speed of Execution:* Multithreaded program can get more done in the same amount of time. Just as the
OS can run a different program when the executing program gets blocked (on a disk read), if another
thread is blocked, another thread may execute.
4. *Modular Structure:* A program that does several different things may be given structure through threads


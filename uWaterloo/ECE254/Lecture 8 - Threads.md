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

## Drawbacks

- No protection between threads in same process: one thread could easily mess with memory being used
by another thread.
- If any thread encounters error, the whole process might be terminated by the OS. If the program has multiple
processes for different parts, then the other processes will not be affected. If the program has
multiple thrads and they share the same process, then any thread encountering an error might halt all.

## Thread States

Each thread has their own state. Model for thread is simpler five-state model. If a process
is swapped out of memory, all its threads will be swapped out. When the process is swapped
in to memory, all the threads will be swapped in. Therefore we do not need to worry about
whether thread is in memory/swapped. 

The transitions work the same way as the state transitions for a process. As with a process,
a thread in any state can transition to terminated even though that is not shown. When a process
is terminated, all its threads are terminated, regardless of state.

## Thread Cancellation

Thread cancellation is when a running thread will be terminated before it has finished its work.
Once the user presses the cancel button on the file upload, we want to stop the upload task.

The thread that we are going to cancel is called the **target** and there are two ways a thread
might get canceled:

1. **Asynchronous Cancellation:** One thread immedietly terminates the target
2. **Deferred Cancellation:** The target is informed it is cancelled. The target is responsible 
for checking regularly if it is terminated, allowing it to clean itself up properly.

A thread can ignore a cancellation if it is deferred cancellation type - why do we choose this?
Suppose thread canceled has some resources. If thread is poorly terminated, the OS may not reclaim
all resources from that thread. Thus a resource might look like it's in use when it's not.

## Thread Types



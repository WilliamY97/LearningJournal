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

Two categories of threads in implementation: *user-level* threads (ULTs) and *kernel-level* threads (KLTs - aka lightweight
process). ULTs run at the user level and KLTs run at kernel level.

There are three possible approaches:

1. All threads are user level
2. All threaDs are kernel level
3. A combination of both approaches

If the operating system in question does not support threads, we can still do multithread programming through user level threads in some sort of threads library. The library does creation, management, and cleanup of threads.

The kernel is unaware of the existence of the user level threads and it is therefore the responsibility of the threads library or the
application to manage the threads.

Three advantages of using user-level threads:

1. Threads switches do not require kernel privileges, because the thread library is in the user-side. We don't need to switch to kernel
mode and back for each thread switch.
2. Scheduling can be something the program decides rather than leaving it to the operating system policy.
3. Portability: the program can run in a multithreaded way even if the kernel does not support multiple threads.

As far the kernel is concerned, there is only one thread for that process. Thus, if any of the threads in the process block (such as 
making I/O request), the whole process will be blocked. There is a solution to this called **jacketing** which is the conversion of a
blocking system call into a non blocking system call.

Instead of calling the system call directly, the program calls the thread library's version of the system call. The jacket routine checks if the request will result in the application being blocked and can decide instead to consider the requesting thread blocked
and switch to another one, preventing the OS from blocking the whole process.

The kernel level threads approach is taken by Windows, for example. The kernel is responsible for all thread management and it overcomes
one of the weaknesses of the ULT approach. If one thread in a process is blocked, the others may continue. Another positive feature is that the kernel routines themselves may be multithreaded.

Disadvantage of this is the opposite of the advantage of the ULT: A thread switch involves entering kernel mode with a ```trap``` and then returning from kernel mode to user mode (takes time).

We can combine both approaches where user/kernel level threads co-exist in the system. This is common as any system that has kernel
level threads can still run applications that use a thread library.

To look at this from another angle, we can consider the relationships between user and kernel level threads, of which we will consider
three: Many To-One, One-To-One, and Many-to-Many.

**Many To-One Model:** In this model, many user level threads are mapped to one kernel thread. Thread management is done in the user space; we see this with ULTs only. 

**One-To-One Model:** This is what happens when there is only KLTs. Creating a new user level thread results immediately in creating
kernel level thread to correspond to it.

**Many-To-Many Model:** This maps many ULTs to smaller or equal number of kernel threads. This approach provides maximal concurrency
in executing a single program.

No **One-To-Many** model because it makes no sense for one user thread to be mapped to multiple kernel threads. It is wasteful for 
a user thread to be served by multipled kernel threads.


# POSIX Threads

```pthread``` refers to the POSIX standard that defines thread behaviour on UNIX/UNIX-like systems (Linux, MAC OS X, etc).
This is a specification document that says how threads should behave. This stanrdard lets code for one UNIX-like system
run easily on another (ex. Linux).

The POSIX standard for pthreads defines something like 100 function calls, but we need not examine all of them. Let us focus
on a few of the important ones and we can see they are, for the most part, very similar to wht we saw with parent and child processes.

```pthread_create``` - Create a new thread. This works a lot like ```fork```.

```pthread_exit``` - Terminate the calling thread. This is like ```exit``` in that it ends execution and returns a value

```pthread_join``` - Wait for a specific thread to exit. This is like ```wait```: the caller cannot proceed until the thread
it is waiting for calls ```pthread_exit```. Note that it is an error to join a thread that has already been joined.

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

```pthread_yield``` - Release the CPU and let another thread run. There is no analagous call for processes
b/c every rpocess is expected to act as if it is the only process in the system.

In case of threads, they all belong to the same program, we expect that threads want to co-operate
rather than compete for CPU time and threads can make decisions about when it would be ideal to let some other thread
run instead.

```pthread_attr_int``` - Create and initialize a thread's attributes. The attributes contain things like
the priority of the thread.

```pthread_attr_destroy``` - Remove thread attributes. Free up memory holding the thread's attributes. This does not
terminate the thread's attributes.

```pthread_cancel``` - Signal cancellation to a thread. This can be asynchronous or deferred, depending on the thread's attributes

We have examine threads on a theoretical level, but have not actually considered how to make something run in the background. Note
that ```main``` is just a function. The way we start a thready is: run this function, but in a new thread.

System call to create a new thread is ```pthread_create``` and its use looks like:

```
pthread_create( pthread_t *thread,
                const pthread_attr_t *attributes,
                void *(*start_routine)( void * ),
                void *argument );
```

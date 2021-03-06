# POSIX Threads

## What are POSIX Threads?

```pthread``` refers to the POSIX standard that defines thread behaviour on UNIX/UNIX-like systems (Linux, MAC OS X, etc).
This is a specification document that says how threads should behave. This stanrdard lets code for one UNIX-like system
run easily on another (ex. Linux).

The POSIX standard for pthreads defines something like 100 function calls, but we need not examine all of them. Let us focus
on a few of the important ones and we can see they are, for the most part, very similar to what we saw with parent and child processes.

## Function Calls in POSIX Threads

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

## Running Something In the Background

We have examine threads on a theoretical level, but have not actually considered how to make something run in the background. Note
that ```main``` is just a function. The way we start a thread is: run this function, but in a new thread.

System call to create a new thread is ```pthread_create``` and its use looks like:

```
pthread_create( pthread_t *thread,
                const pthread_attr_t *attributes,
                void *(*start_routine)( void * ),
                void *argument );
```

```Thread``` is a pointer to a ```pthread``` identifier and will be assigned a value when the thread is created.

The attributes ```attr``` may contain various characteristics (you may supply NULL if you want the defaults). The
```start_routine``` is any function that takes a single untyped pointer and returns an untyped pointer.

Finally, the last parameter, ```arguments``` is the argument passed to the ```start_routine```

After the new thread has been created, the process has two threads in it. The OS makes no guarantee about
which thread will be executing after the new one is created; this is matter of scheduling. It could be
either of the threads of the process, or a different process entirely.

It is normal to have a single return value from a function, but it seems limiting to be able
to put in just one parameter. There are two ways to get around this: with an array or with structures
```struct```. In the case of array, the argument provided to ```pthread_create``` is just a pointer to
the array.

This is also, how you get multiple return values out of a function in JAVA / C#, but not recommended.

The other way is to use the ```struct``` as below, defining a structure for the parameter type and one
for the return type. In the example, all four variables are integers, but they could be of any type.

```
typedef struct {
  int parameter1;
  int parameter2;
} parameters_t;

typedef struct {
  int return1;
  int return2;
} return_t;
```

The function that is to run in the new thread must expect a pointer to the arguments rather than
explicity arguments: ```void* function( void *args ) ``` which can then be cast to the appropriate type:
```parameters_t * arguments = (parameters_t*) args;```

What about the thread attributes? They can be used to query or set specific attributes of the thread, such as:

- Detached or joinable state
- Scheduling data (policy, parameters, etc...)
- Stack size
- Stack address

The first item in that list indicates if a thread is joinable or detached. By default,
new threads are usually joinable (other thread can call ```pthread_join``` on them).

As noted before, it is a logical error to attempt multiple joins on the same thread. To
prevent a thread from ever being joined, it can be created in detached state (or the method
```pthread_detach``` can be called on a joinable thread).

Trying to join a detached thread is also a logical erorr.

The use of ```pthread_exit``` is not the only way a thread may be terminated. Sometimes we
want the thread to persist (hang around), but if we want to get a return value form the thread, then
we need it to exit. Like the ```wait``` system call, the ```pthread_join``` is how we get a value
out of the spawned thread:

```
pthread_create( &thread_id, NULL, function_name, &args );

// This function and the created function are now running in parallel
void *void_ret;

pthread_join( thread_id, &void_ret );

return_t *returnValue = (return_t *) void_ret;
```

If a thread has no return values, it can just ```return``` NULL; which will have same
effect as ```pthread_exit``` and send NULL back to thread that has joined it. If the function
that is called as a task returns normally rather than calling the ```exit``` routine, the
thread will still be terminated.

Another way a thread might terminate is if the ```pthread_cancel``` function is called with it as the target. As before, if the termination is deferred rather than asynchronous, the thread is responsible for cleaning up after itself before it stops.

**A thread may be terminated indirectly:** if the entire process is terminated or if ```main``` finishes first (without calling ```pthread_exit``` itself). Indeed, ```main``` can use ```pthread_exit``` as the last thing that it does. Without that, ```main``` will
not wait for other, unjoined threads to finish and they will all get suddenly terminated. If ```main``` calls ```pthread_exit``` then it
will be blocked until the threads it has spawned have finished.

## Code Example: Summation of a non-negative integer

Let us examine a slightly more complex example that invokes more of the pthread system calls. The code sample below provides an example of a multithreaded C program that uses pthreads to calculate the summation of a non-negative integer in a second thread.

```
#include <pthread.h>
#include <stdio.h>
int sum; /* this data is shared by the thread(s) */
void *runner(void *param); /* threads call this function */
int main(int argc, char *argv[]) {
pthread_t ti; /* the thread identifier */
pthread_attr_t attr; /* set of thread attributes */
if (argc != 2) {
fprintf(stderr,"usage: a.out <integer value>\n");
return -1;
}
if (atoi(argv[1]) < 0) {
fprintf(stderr, "%d must be >= 0\n", atoi(argv[1]));
return -1;
}
/* get the default attributes */
pthread_attr_init(&attr);
/* create the thread */
pthread_create(&tid, &attr, runner, argv[1]); /* wait for the thread to exit */
pthread_join(tid, NULL);
printf("sum = %d\n", sum);
}
/* The thread will begin control in this function */
void *runner(void *param) {
int i, upper = atoi(param);
sum = 0;
for (i = 1; i <= upper; i++) {
sum += i;
}
pthread_exit(0);
}
```

In this example, both threads share the variable ```sum```. We have some co-ordination here because the parent thread joins the newly-spawned thread (wait until finished) before it tries to print out the value. If it did not **Join** the spawned thread, the parent
thread would print out the sum early. This is yet another example of that subject that keeps popping up: **co-ordination**.

## The ```fork``` and ```exec``` System Calls

```fork``` results in a parent process spawning a child that is a clone of the parent. We expect that ```fork``` makes duplicated of all
of the threads of parent process. Except a child might call ```exec``` and replace self with another program (throwing away all the threads). Then all work to duplicate threads is wasted. Some UNIX systems approach this by having two different implementations of ```fork```, one that will copy all threads and one that will copy only the executing thread.

## Signals

UNIX systems use signals to indicate events (ex. Ctrl-C), which is a form of event-driven programming. Signals also are things like
exceptions (div by zero, segmentation fault), etc. A signal may be *synchronous* if it occurs by program execution or *asynchronous* if
it comes from outside of process (ex. sending signal from one process/thread to another).

**Signals are interrupts with certain interger IDs.**

## Signal Examples

1. ```SIGHUP``` - Hangup detected - Value 1 - Default Action: Terminate Process
2. ```SIGINT``` - Keyboard Interrupt - Value 2 - Default Action: Terminate Process
3. ```SIGQUIT``` - Quit from Keyboard - Value 3 - Default Action: Terminate Process, dump debug info

## Alternative to Handling Signals

Process may inform the OS it is prepped to handle the signal itself (such as doing cleanup when Ctrl-C is received instead of just dying). In any event, a signal needs to be handled, even if the handling is to ignore it.

Note that SIGKILL and SIGSTOP cannot be caught, blocked, or ignored.

## Difficulty in Multithreaded Program

Which thread should the signal be sent? In general there are the following options:

1. Deliver the signal to the thread to which the signal applies
2. Deliver to every thread in process
3. Deliver the signal to certain threads in process
4. Assign a specific thread to receive all signals for process

Which method for signal distribution is dependant on the signal. Synchronous signals will be sent to the thread that triggered the signal, but the process could handle asynch signals in any of the four ways.

UNIX threads allow a thread to say what signals it will accept. If delivered to a process, the first thread that can handle it will
accept it. Thread can redistribute the signal to other threads if necessary.

In UNIX, to deliver a signal to a process, the command is:
```kill( pid_t pid, int signal )```

Yes, to send a signal, event if it's not a kill signal, the command is kill. The equivalent in POSIX pthreads is:
```pthread_kill( pthread_t tid, int signal )``` where it will deliver the signal to a specific thread.

## Command Line Operation

On command line, the command to send a signal is also ```kill``` followed by a process ID. Normally a command like ```kill 24601``` will
send SIGHUP to a process, which will, by default, kill process.

Process has opportunity to clean things up if it wants to. If it's still stuck you can force kill the process by sending SIGKILL with
the command ```kill -9 24601```. The ```-9``` parameter says to send signal ```9``` (SIGKILL) rather than the default 1 (SIGHUP).

## Cancellation

Pthread command to cancel a thread is ```pthread_cancel``` and it takes one parameter (the thread identifier). By default, a pthread is
set up for deferred cancellation. In the function tha runs as a thread, to check if the thread has been cancelled, the function call is
```pthread_testcancel``` which takes no parameters.

Suppose your background tasks is to upload a bunch of files, consecutively. It is good practise to check ```pthread-testcancel``` at the
start or end of each iteration of the loop, and if cancellation has been signalled, clean up open files and network connections and then
```pthread_exit```. Thus, if the thread has been told to cancel, it will do as it is told in short time.

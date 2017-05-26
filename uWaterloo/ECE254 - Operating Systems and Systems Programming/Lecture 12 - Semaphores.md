# Lecture 12 - Semaphores.md

## Mutual Exclusion through Messages

Earlier definition of mutual exclusion said only one thread may be in the critical section at a time. This is
the minimum, but there are additional desirable properties that will be used to evaluate any solution:

1. Mutual exclusion must apply (this criterion eleminates most flag examples)
2. A thread halting outside of critical section should not interfere with other threads
3. It must not be possible for a thread requiring access to a critical section to be delayed
indefinitely (threads get stuck, each thinking other is in critical section)
4. When no thread is in the critical section, a thread requesting access should be able to
enter right away (no unneeded waiting)
5. No assumption about what thread will do or # of processors in the system (so it should
be a general solution
6. a thread remains inside the critical section for a finite time only (this is more
an assumption than criterion), but our solution must provide a way to indicate the thread
has left the critical section.

A good strategy would be for Event A to leave a message for Event C, letting A know when
Event C is done. A can then do its own work until C calls.

**Busy Waiting** is bad since it wastes CPU time that another process/thread could be putting
to productive use. Periodic is bad for computer too. Also could be wasting time if period is longer
than an event takes to finish.

The call-when-finished semantics of leaving a message and calling back is called a **Semaphore**.

## Semaphore

Definition: A system of signals used for communication.

**Binary Semaphore**: A variable that has two values, 0 and 1. It can be initialized to 0 or to 1.
The semaphore has two operations: ```wait``` and ```signal```.

```wait``` - Operation on semaphore is how a program tries to enter the critical section. When
```wait``` is called, if he semaphore is 1, set it to 0 and this thread may enter the critical
section and continue. If sema is 0, some other thread is in the critical section and the current
thread needs to wait. The thread that calls ```wait``` will be blocked by OS. AKA Decrementing semaphore

```signal``` - How a program indicates it is finished with critical section. When this is called,
if a semaphore is 1, do nothing. If semaphore is 0, and there is a task blocked awaiting that sema,
that task may be unblocked, else set the sema to 1. AKA Incrementing semaphore

OS is needed to make this work - if thread A attempts to wait on a sema that some other thread already has,
it will be blocked and the OS knows not to schedule it to run until it is unblocked. When thread B is
finished and signals the sema it is holding, that will unblock a and allow it to run again.

Sema does not provide facility to check the current value. A thread doesn't know in advance if it will
block when it waits on a semaphore. It can only wait and may be blocked or may proceed directly into
the critical section if there is no other thread in there at the moment.

When a thread signals a semaphore, it likewise does not know if any other thread(s) are waiting on that
semaphore. THere is no facility to check this, either. When thread A signals a semaphore, if another thread B is waiting,
B will be unblocked and either thread A or thread B may continue execution or another unrelated thread may be
the one to continue execution.

## Bad Behaviour in Semaphore

There is nothing in semaphore that protects against bad behaviour. Suppose a thread C wants to enter
the critical section. Even though A or B might be in the critical section, the sema gets signalled
so he is more or less certain that his program will now get to enter the critical section. This is bad.

This problem is solved by supporting the basic binary semaphore. A data structure called a mutex is
a binary semaphore with an additional rule that only one thread that has called ```wait``` may ```signal```
that semaphore. This adds a small amount of extra bookkeeping to the semaphore, but is reasonable.

## Binary Semaphore Syntax

```semaphore_init( semaphore_t *sem, int i )```
Initialize the semaphore to i (can be 0 or 1)





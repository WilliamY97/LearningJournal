# Lecture 13 - Synchronization Patterns

# Synchronization Patterns

Number of common synchronization patterns that occur frequently and we can use semaphores to solve them. These
synchronization patterns are ways of co-ordinating two threads of processes. We have already examined serialization
and mutual exclusion, but there are many more.

## Signalling

Signalling can be used as a general way of indicating that something has happened. Suppose
we have a semaphore that something has happened. Suppose we have a semaphore named ```sem```, initialized to 0.

```
Thread A
1. Statement A1
2. signal( sem )

Thread B
1. wait( sem )
2. Statement B2
```

If B gets to the ```wait``` statement first, it will be blocked (as the sem is 0) and cannot
proceed until someone signals on that semaphore. When A does call ```signal```, then B may
proceed. If instead A gets to the signal statement first, it will signal and the semaphore
value will be 1. Then, when B gets to the ```wait``` statement, it can proceed without
delay. Regardless of the actual order that the threads run, we are certain that statement A1
will execute before statement B2.

Note that this is a situation where it makes sense for a thread to signal a semaphore even if it
is not the thread that waited on that semaphore. Thus sometimes, the semaphore is appropriate
and the mutex structure is not necessary in every circumstance.

## Rendezvous

AKA Two threads should be at the same point before either of them may proceed (meet up). The
desirable property is that A1 should take place before B2 and that B1 should take place before
A2. As each thread must wait for the other, we need 2 semaphores. One to indicate that A has 
arrived and one for B. We will assigned them the names ```aArrived``` and ```bArrived``` and
initialize both to 0. A first attempt:

```
Thread A
1. Statement A1
2. wait( bArrived )
3. signal( aArrived )
4. Statement A2

Thread B
1. Statement B1
2. wait( aArrived )
3. signal( bArrived )
4. Statement B2
```

**Problem**: Thread A gets to the ```wait``` statement and will wait until B signals its arrival
before it can proceed. Thread B gets to ```wait``` statement and will wait until A signals its
arrival before it will proceed. Unfortunately, each thread is waiting for te other to signal
and neither of them can get to the actual ```signal``` statement because they are both blocked.

Neither thread can proceed. The situation can never be resolved, because there is no external
force that would cause one or the other to be unblocked. This situation is **deadlock**.

How about:

```
Thread A
1. Statement A1
2. signal( aArrived )
3. wait( bArrived )
4. Statement A2

Thread B
1. Statement B1
2. signal( bArrived )
3. wait( aArrived )
4. Statement B2
```

This solution works: A gets to rendezvous point first, it signals its arrival and waits for B. If B
gets there first, it signals its arrival and waits for A. Whichever gets there last signal and unblock
the other, before it calls wait and will be able to proceed directly because the first thread to arrive 
already signalled.

A variation on this can also work where only one thread signals first and the other thread signals second. This is
shown below:

```
Thread A
1. Statement A1
2. wait( bArrived )
3. signal( aArrived )
4. Statement A2

Thread B
1. Statement B1
2. signal( bArrived )
3. wait( aArrived )
4. Statement B2
```

Less efficient though than previous: it may require an extra switch between processes. If A arrives
at the ```wait``` statement, it waits then B signals and must then wait for A's signal (it cannot
proceed right away even though it got there second). After A gets to run again it may proceed to
signal and unblock B. For the most part, we are usually satisfied as long as we are certain the 
deadlock will not occur that a given solution is acceptable.

## Mutual Exclusion


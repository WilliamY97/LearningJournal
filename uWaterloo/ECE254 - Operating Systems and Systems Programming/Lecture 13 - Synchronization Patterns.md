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

```
Thread A
1. wait( mutex )
2. critical section
3. signal( mutex )

Thread B
1. wait( mutex )
2. critical section
3. signal( mutex )
```

The mutex semaphore is originally initialized to 1 (unlike the previous examples where it started at 0), so whichever thread gets to
the ```wait``` statement first will proceed immediately and not be blocked at all. If the semaphore were initialized to 0 then neither
thread could ever get to the ```signal``` statement or ever get into the critical section (deadlock).

Both threads A and B are identical here, which was not always the case in previous examples. This is a **symmetric solution**. It is 
easier to make predicitons about the behaviour of the threads when they all do the same thing. If the different threads have different sections of code, they are **asymmetric**.

The symmetric solutions very often scale well: we could have arbitrarily many threads executing in that same pattern, as long as they
all wait on the semaphore before entering the critical section, we can be sure mutual exclusion is enforced.

## Multiplex

If the general semaphore is initialized to n, then at most n threads can be in the critical section at a time. This pattern is common.
This is a symmetric solution, so it will work for arbitrarily many threads.

```
Thread K
1. wait( mutex )
2. critical section
3. signal( mutex )
```

The only difference between this and mutual exclusion is how many threads can enter the critical section at a time (1 vs many)

## Barrier

Barrier pattern is a generalization of the rendezvous pattern; a way of having more than two threads meet up at the same point before any can proceed. Given ```n``` threads (each knows total # of threads), when first ```n-1``` threads arrive, they should wait until the
nth arrives.

We might consider a variable to keep track of the number of threads that have reached the appropriate point. B/c this variable is shared
data, modification of it should be in a critical section. Thus we will have a sempahore, initialized to 1, called ```mutex``` to protect
that counter. Then we will have a second sempahore, ```barrier``` that will be the place where threads wait until the ```nth``` thread arrives.

```
Thread K
1. wait( mutex )
2. count++
3. signal( mutex )
4. if count == n
5. signal( barrier )
6. end if
7. wait( barrier )
```

## Problem with Barrier
When the nth thread arrives, it unlocks the barrier (signals it) and then proceeds. This is not a solution b/c it will lead to stuck threads (permanent). If there is more than one thread waiting at the barrier, the first thread will be unblocked when the nth thread signals it. However, after that, there are no other ```signal``` statements and therefore the other threads waiting are stuck forever,
waiting for signal that never comes.

It should probably signal n-1 times.

```
Thread K
1. wait( mutex )
2. count++
3. signal( mutex )
4. if count == n
3
5. for i from 1 to n-1
6. signal( barrier )
7. end for
8. end if
9. wait( barrier )
```

This is a solution that allows all of the n threads to proceed (none get stuck), but it is less than ideal. The thread that runs last is
very likely the lowest priority thread (if it were high priority it would likely have run first) and therefore when it signals on the
semaphore, the thread that has just been unblocked will be the next to run. Then the system switches back, at some later time, to the
thread currently blocking all the others. Worst case is 2n process switches, when it could be accomplished with just n. Have each
thread unblock the next:

```
Thread K
1. wait( mutex )
2. count++
3. signal( mutex )
4. if count == n
5. signal( barrier )
6. end if
7. wait( barrier )
8. signal( barrier )
```

This pattern of a wait followed by a signal is a common pattern called a ```turnstile``` (like the subway ticket entrance).

**Turnstile** patten allows one thread at a time to proceed through, but can be locked to bar all threads from proceeding. Initially
the turnstile in the above example is locked, and the nth thread unlocks it and permits all n threads to go through.

Alert readers may have noticed something that causes some distress -> line 4 we read value of count (shared value) without a semaphore to protect it. Dangerous, but the alternative:

```
1. wait( mutex )
2. count++
3. if count == n
4. signal( barrier )
5. end if
6. wait( barrier )
7. signal( barrier )
8. signal( mutex )
```

Has deadlocked again. The first thread waits on ```mutex``` and then goes to wait on the ```barrier``` semaphore. At this point, the
first thread is blocked. When a second thread comes along it will wait on ```mutex``` but can get no further because the first thread
has not signalled it.The counter will be 1, but cannot get past 1.

The condition of ```count``` equalling ```n``` can never be true. Thus all the threads are stuck. This is a common source of deadlock:
blocking on a semaphore while inside a critical region.

## The Reusable Barrier

Barrier solution is good, but count can only increase but never go down. Once the barrier is open it can never be closed again. Programs
very often do the same thing repeatedly, so a one-time use barrier is not ideal; it would be better to have reusable barrier. The
way to deal with this is to decrement ```count``` after the rendezvous has taken place. The line labelled ```critical point``` is
the section of that must wait until all the threads have rendezvoused.

```
Thread K
1. wait( mutex )
2. count++
3. signal( mutex )
4. if count == n
5. signal( turnstile )
6. end if
7. wait( turnstile )
8. signal( turnstile )
9. [critical point]
10. wait( mutex )
11. count--
12. signal( mutex )
13. if count == 0
14. wait( turnstile )
15. end if
```

There are two problems with the above implementation. Suppose thread ```n-1``` is about to execute line 4 (the comparison of ```count```) and then there is a process switch and the nth thread comes to this point. Both of them will find that ```count```
is equal to ```n``` and therefore both threads will signal the turnstile. The same problem occurs on line 13: more than one
thread may wait on the turnstile, resulting in deadlock:

```
Thread K
1. wait( mutex )
2. count++
3. if count == n
4. signal( turnstile )
5. end if
6. signal( mutex )
7. wait( turnstile )
8. signal( turnstile )
9. [critical point]
10. wait( mutex )
11. count--
12. if count == 0
13. wait( turnstile )
14. end if
15. signal( mutex )
```

This solves the problem previously identified by putting the checks of ```count``` inside the critical section controlled by ```mutex```. There is another problem that can occur here: suppose one particular thread gets through the second mutex but is running
in a loop and gets back through the first mutex again. This would be like on thread being one lap ahead of others. We can prevent this
by having two turnstiles: first all threads wait at the first tunrstile until the last gets there and lets them through. Then all threads wait at a second turnstile until the last gets there and lets them all through again. 

```
Thread K
1. wait( mutex )
2. count++
3. if count == n
4. wait( turnstile2 )
5. signal( turnstile1 )
6. end if
7. signal( mutex )
8. wait( turnstile1 )
9. signal( turnstile1 )
10. [critical point]
11. wait( mutex )
12. count--
13. if count == 0
14. wait( turnstile1 )
15. signal( turnstile2 )
16. end if
17. signal( mutex )
18. wait( turnstile2 )
19. signal( turnstile2 )
```

This solution can also be called a ```two-phase barrier``` because all threads have to wait twice: once at each turnstile.

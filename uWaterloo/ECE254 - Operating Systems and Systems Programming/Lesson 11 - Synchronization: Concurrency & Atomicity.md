# Lesson 11 - Synchronization: Concurrency & Atomicity

## Synchronization

**What would happen if we had no concurrency?**

That would mean we would be doing things one thing at a time (one process and thread). We would have no coordination problems.

We have seen that a system with multiple processes or threads has concurrency. If the system is multicore, we can have parallelism: more than
one thread or process actually executing on a CPU in a given instant. Either or both can lead to problems.

**Difference between concurrency and parallelism**

**Concurrency** is the interleaving of processes in time to give the appearance of simultaneous execution. Thus it differs from **parallelism**, which offers genuine
simultaneous execution.

## Actions of the OS

The author of an application doesn't decide when a thread runs or switch occurs. These are done by the OS which does not give much though
to whether it is a convenient or inconvenient time to run a given thread.

**Synchronization**: We want some relationship between events, and it can be before, during, after.

**Serialization**: We want there to be some sort of order of events (Event A before Event B). 

**Mutual Exclusion**: Events C and D cannot happen at same time. In inter-process communication, if two processes can write to this area
there is some possibility that they both try to access the same place at the same time. If we have mutual exclusion this can't happen.

## Serialization through Messages

We need serialization in the case that Event A must happen before Event B

If we are certain that one happens before another - we can say that the events are **sequential** because we know order of events.

In the case that some point Event A occurs and some time before Event B occurs - then we have no idea who occured first.

**Concurrent:** Two events are concurrent if we cannot tell by looking at the program which will happen first.

When we say something happene concurrently - they happend at the same time. In this context, it's not like saying they happened at the
same time. It's saying we don't know an order of events. It's possible they occur at the same time.

The order of concurrent events may change on two runs of the program; this is what we call **nondeterminism**.

**What is non-deterministic program then?**

We cannot tell just by looking at non-deterministic program what the execution order would be. This makes it hard to analyze a program.

AKA Heisenbug - harder we track down, the less likely for it to occur.

## Shared Data and Atomic Operations

The need for co-ordination in interprocess communication arises from fact that some area of memory is shared. We know that all
threads of a process share the same data. 

```
Thread A
A1. x = 5
A2. print x

Thread B
B1. x = 7
```

This is non-deterministic code because there is no co-ordination mechanism so we don't know which order they will occur.

This example uses more than one thread, but we could still get a concurrency problem without them. Having interrupts in the system
is sufficient.

Ex. A reset button might be clicked during the intricasies of a counter and so the counter is still set to the next value instead of 0.

**Atomic**: An operation that cannot be interrupted.

We know some operations available are atomic, but we are not certain. We need to make sure at the very least one operation on the shared variable is finished before the next begins.

## Can we fix this issue with serialization?

The idea being to make sure that ```count++``` operation completes before the ```count = 0``` operation? That would eliminate the problem of the reset being ignored. Our concept of serialization requires that there exists a correct order. Here, where both orders
are valid, we need another approach: **mutual exclusion** (mutex).

With mutex, we do not know or enforce any particular order of events, but what we do is make sure no multiple threads are trying to update the variable at the same time. It would mean the action to reset ```count``` to zero would have to wait until the ```count++```
operation was completely finished (or vise versa) before it gets to execute.

TLDR; We don't need a necessary order - just make sure they don't happen at same time.

## Mutual Exclusion through Flags

We have identified shared data as a potential source of error. A section of code that should be accessed by a maximum of one thread
at a time is referred to as a ```critical section```. The purpose of mutual exclusion is to make sure only one thread is in the
critical section at a time. Can't have more than one thread in it or not allowing any thread in it ever.

Responsibility of programmer to protect critical sections with mutexes. Critical section cannot be run in parallel so it increases
the magnitude of the S term in Amdahl's law, limiting the speed incrase we can get from multiple threads and cores.

Our first approach is to indicate when the critical section is not in use:

```
Thread A
A1. while ( turn != 0 ) {
A2. /* Wait for my turn */
A3. }
A4. /* critical section */
A5. turn = 1;

Thread B
B1. while ( turn != 1 ) {
B2. /* Wait for my turn */
B3. }
B4. /* critical section */
B5. turn = 0;
```

This scheme enforces strict alternation. Turn of thread A then B, then back to A, so on. What if A is run more than B? If thread
B terminates then thread A is stuck forever.

Another approach:

```
Thread A
A1. while ( busy == true ) {
A2. /* Wait for my turn */
A3. }
A4. busy = true;
A5. /* critical section */
A6. busy = false;

Thread B
B1. while ( busy == true ) {
B2. /* Wait for my turn */
B3. }
B4. busy = true;
B5. /* critical section */
B6. busy = false;
```

The problem with flags is that when we have a statement like ```while (busy==true)``` followed by busy = true; these are two steps
and a process switch can occur between the read and the write. If the switch happens at the bad time then thread A and B will
both be in critical section at the same time. This solution is not great.

**What if instead of using one flag variable, we use an array where each thread writes to its own boolean variable?**

```
Thread A
A1. flag[0] = true;
A2. while ( flag[1] ) {
A3. /* Wait for my turn */
A4. }
A5. /* critical section */
A6. flag[0] = false;

Thread B
B1. flag[1] = true;
B2. while ( flag[0] ) {
B3. /* Wait for my turn */
B4. }
B5. /* critical section */
B6. flag[1] = false;
```

Strategy is still defeated by untimely process switch. If statement A1 sets flag[0] to true and there is switch so thread B sets
flag[1] to be true, now both processes are stuck. Neither can advance because each is waiting for other to set its ```flag``` variable
to false.

A bit better than two threads in the critical section, but we have two threads that are perma stuck now. Both are waiting for other
thread to set its flag to false. Better than two threads in critical section though.

The attempts at solution we have attempted so far have all been foiled by an untimely process switch, which will
be triggered by an interrupt.

## Why Removing Interrupts is a bad idea

We could disable interrupts but then interrupts made by user as well as normal thread switches the scheduler performs will not occur.

The system would be unable to respond to user input or other events. If an error encountered in the critical section and the program is
terminated, the system is effectively stuck b/c no other program is able to run.

It gets worse: if we have multiple processors the disabling interrupts will not be sufficient.

## Test-and-Set

Test-and-Set instruction is a special machine instruction that is performed in a single instruction cycle and istherefore not interruptible. T and S will return a boolean value.

Finally, we have something that will provide mutual exclusion without the risk that the threads will all get stuck because each thinks another is in the critical section.

The while loop that is constantly checking the value with the Test-and-Set instruction is an example of ```busy-waiting```.

Thread A will not get into the critical section while thread B is in there and asking constantly does not make B get the job done any faster, just as a child asking “are we there yet?” does not improve the speed at which he or she gets to his or her destination

Less wasteful of resources and effort if the while loop contains some instructions saying it should wait a little before re-checking.

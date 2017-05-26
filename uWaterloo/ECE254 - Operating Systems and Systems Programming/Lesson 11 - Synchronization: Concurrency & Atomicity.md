# Lesson 11 - Synchronization: Concurrency & Atomicity

## Synchronization

**What would happen if we had no concurrency?**

That would mean we would be doing things one thing at a time (one process and thread). We would have no coordination problems.

We have seen that a system with multiple processes or threads has concurrency. If the system is multicore, we can have parallelism: more than
one thread or process actually executing on a CPU in a given instant. Either or both can lead to problems.

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

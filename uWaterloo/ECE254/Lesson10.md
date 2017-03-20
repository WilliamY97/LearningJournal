# Lecture 10 - Symmetric Multiprocessing (SMP)

## Multiprocessing

- A quad-core processor may be executing four different instructions from four different threads at the same time.
- In theory multiple processors means we can get more work done in the same amount of (wall clock) time, but this is not
a guarantee. If one of the CPUs in a two-CPU system fails, the system can carry on at a reduced performance level.

## Asymmetric Multiprocessing Vs. Symmetric Multiprocessing Systems

**Asymmetric**: There is a boss processor that is in charge of controlling the system: all other processors are workers
and they take instructions from the boss or have a specific task to perform.

**Symmetric**: The other kind of system, symmetric, is more collectivist: the wokrers are in charge and all processors are equal

- Most systems we use (laptops, phones, etc) are symmetric multiprocessing (SMP), but in theory whether a system is symmetric or
asymmetric can be configured in software.

Formal Definition of SMP:

1. There are two or more general purpose processors
2. The processors share the same main memory and I/O devices and are interconnected by a bus
3. All processors are capable of performing the same functions
4. The system is controlled by an OS that provides interaction between processors and their programs

- We often refer to logical processing units as a **core**. The term CPU may refer to a physical chip that has one or more
logical processing units (cores).

## What to do when more processes and threads than available cores?

- We can hope that the processes get blocked frequently enough and long enough that all processes get to run, but this is not
somethign we can count on.

## Time Slicing

- Solution is that the CPU should switch between different tasks via a procedure we call time slicing. So thread 1 would execute
for a designated period, such as 20 ms, then thread 2 for 20 ms, then thread 3 for 20 ms, then back to thread 1 for 20 ms. To
the user it seems like they're running parallel.

## Parallelism and Speedup



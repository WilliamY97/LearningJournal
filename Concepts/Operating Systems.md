# Operating Systems

Note: In-depth study of OS in https://github.com/WilliamY97/LearningJournal/tree/master/uWaterloo/ECE254%20-%20Operating%20Systems%20and%20Systems%20Programming

## What Is An Operating System?

Computing systems consist of a number of hardware components. This includes one or more processing elements (processors or CPU's). There
is also memory, devices like network interconnects (Ethernet / Wifi Card), Graphics Processing Cards (GPU's), and also storage devices like
hard disks, SSDs, and flash devices like USB drives. **All of these components are used by several applications.**

- An operating system is the layer of systems of software that sits between the complex hardware and all these applications.

## Purpose

- Hides hardware complexity from both applications, and application developers. 

- Resource Management, helps figure out which one of the hardware resources each application uses and how much. (Ex. Allocates memory)

- Provide isolation and protection, make application's not access each other's memory, 

# Process 

- Instance of an executing program (synonomous with "task" or "job")
- Has 3 major components: 1. Executable Program, 2. data created/needed by the program, 3. execution context of the program (files opened, resources allocated)

## What Is A Process

- An application is a program on a disk, flash memory (static entity). A **process** is a state of a program when executing loaded in memory (active entity).

Ex. A process can be one instance of the word editor program 

# Threads

- A short form for **Thread of Execution**. A sequence of executable commands that can be schedule to run on the CPU. With one thread
you are executing one statement at a time.

## Motivation for Threads

- Why choose threads rather than a new process? The primary, but not sole, motivation is performance.

1. Creating a thread is faster than creating a process (10x faster)
2. Terminating/cleaning up a thread is faster than cleaning up a process
3. Takes less time to switch between two threads within same process (less data needs to be stored/restored).
4. Threads share same memory space, for two threads to communicate, they do not use any of the IPC mechanisms, they can communicate directly.
5. Use of threads allows program to be responsive even when a part of the program is blocked

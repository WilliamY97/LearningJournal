# Lecture 4 - Processes

- A **process** is a program in execution. It more than than just compiled instructions. A process is three things:

1. The instructions and data of the program (the compiled executable).
2. The current state of the program
3. Any resources that are needed to execute the program

Basically everything the OS does involves or more processes and all the other concepts we examine will depend on this subject.

Most requirements of an operating system revolve around processes.

**Scheduling::** The OS must choose which process run at what time, to maximize processor
utilization and/or minimize response time

**Resource Allocation:** The OS must allocate resources to processes, keeping track of what
resources are owned by which process

**Inter-process CommunicationL** The OS must support inter-process communication: the transfer of data from one
process to another (by whatever means).

Two instances of the same program counts as two seperate processes.

## The Process Control Block

The operating system's data structure for managing processes is the **Process Control Block** (PCB). This is a
data structure containing everything the OS needs to know about the program. It is created and updated by the OS
for each running process and can be thrown away when the program has finished executing and cleaned everything up.

The blocks are held in memory and maintained in some container (ex. a list) by the kernel.

The PCB will have:

**Identifier** - A unique ID associated with the process
**State** - The current state of process
**Priority** - How important this process is (compare to the others)
**Program Counter** - A place to store address of the next instruction to be executed
**Register data** - A place to store the current values of the registers (called context data)
**Memory Pointers** - Pointers to the code as well as data associated with this process, and any memory the OS has allocated by request
**I/O Status Information** - Any outstanding requests, files, or I/O devices currently assigned to this process
**Accounting Information** - Some data about this process's use of resources. Optional

## The Circle of Life

Processes may be created and destroyed.

- Upon creation, the OS will create a new PCB for the process and initialize the data in that block
- This is setting the variables to their initial values: setting initial program state, instruction pointer to first instruction
in Main, and so on.

PCB will be then added to PCBs the OS maintains. After the program is terminated and cleaned up, the OS may collect some data
and then it can remove the PCB from the list of active processes and carry on.

## Process Creation

Three main events that lead to creation of process:
1. System boot up
2. User request to start new process
3. One process spawns another

Ex. embedded system might have all processes it will ever run created by initialization process

- OS starts up various processes - some in foreground/background. The UNIX term for background process is ```Daemon```

- When an already-executing program spawns another process, we say the spawning process is the parent
and the one spawned is the child.

## Process Destruction

Four ways for process to die:
1. Normal exit (voluntary)
2. Error exit (voluntary)
3. Fatal error (involuntary)
4. Killed by another process (involuntary)

- Restrictions to killing - a user/process must have rights to execute the victim
- When a process is killed - all processes spawned are killed as well

## Process Family Tree

- A process and all its descendants form a **Process Group**
- Process may have one parent, but zero or more children

- In UNIX, first process created is ```init``` and it is the parent of all processes (eventually),
thus in UNIX we may represent all processes as a tree structure, where each node is a process, eac node may
have zero or more children, and moving up the hierarchy will eventually take us to ```init```

- In windows, a process spawns another process gets a reference to its child, allowing it 
to exercise some measure of control over the child. However reference may be given to another
process (adoption exists) meaning there is no real hierarchy. UNIX cannot disinherit a child.

- When process terminates, it does so with return code. UNIX parent process spawns a child,
it can get the code the process returns. A return value indicates success and other values indicate
an error of some sort. There is understanding between parent/child processes about what a code means.

- Child process finishes execution, until such time the parent comes to get return value,
the child continues in state of 'undeath' we call a ```zombie```. Dead but not gone. Still an entry
in the PCB list and the process holds on to its allocated resources until such time as the return value
is collected. 

- Usually, a child process's result is eagerly awaited by its parent and the ```wait``` call collects the value
right away, allow child to be cleaned up. If there is delay, the child is a zombie.

- If parent process dies before child, the process is called an ```orphan```. In UNIX, any
orpgan process is auto-adopted by ```init``` process. By default, ```init``` will just ```wait```
on all its child processes (and do nothing with return value) - ensuring they do not become zombies.

- Sometimes processes are intentionally orphaned; it is spawned to run in background.

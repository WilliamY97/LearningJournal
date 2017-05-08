# Lecture 5 - Process State

The OS is responsible for determining which programs run when and how to allocate resources.
The current state of the process is therefore important information. To maintain the state of the
process the PCB has a variable, but we will think about this as a finite state machine (FSM): there
are limited number of states and defined transitions between them.

## The Two-State Model

- Either a process is executing, or it is not. Two states:

1. **Running**: Actively executing right now
2. **Not Running**: Not currently executing

- When new process is created, PCB allocated and the state of the process is Not Running

Following Transitions:
**Create** - The process is created and enters the Not Running state.
**Dispatch** - A process that is not currently running begins executing amd moves to Running state
**Suspend** - A running program pauses execution, for whatever reason, and moves to Not Running state
**Exit** - A running program finishes, reaches the ```exit```, and can be removed from list of processes.

Inadequate model - assumes every process is constantly ready to run, which is not safe assumption. Need
way to indicate process is not ready to run.

## Three-State Model

- Program that requests a resource like I/O or memory may not get it right away. This is not to
say the program will never get it, just that it does have it right now.

1. **Running**: Actively executing right now
2. **Not Running**: Not currently executing
3. **Blocked**: Not running, and not able to run until some event happens

- Blocked indicates the program is not ready to run because of lack of resources.

Following Transitions:
**Create** - The process is created and enters the Not Running state.
**Dispatch** - A process that is not currently running begins executing amd moves to Running state
**Suspend** - A running program pauses execution, for whatever reason, and moves to Not Running state
**Exit** - A running program finishes, reaches the ```exit```, and can be removed from list of processes.
**Block** - A running program requests a resource, does not get it right away, cannot proceed
**Unblock** - A program, currently blocked, receives the resource it was waiting for, it moves to Ready state.

## Five-State Model

- Unix process might be in zombie mode because parent didn't come to collect it
- Process is thus not ready to run and is not waiting for resource. 
- We need state to represent that it is finished but not yet cleaned up: Terminated

1. **Running**: Actively executing right now
2. **Ready**: Not running, but ready to execute if selected by the schedule
3. **Blocked**: Not running, and not able to run until some event happens
4. **New**: Just created but not yet added to the list of processes ready to run
5. **Terminated**: Finished executing but not yet cleaned up (reaped).

Following Transitions:
**Create** - The process is created and enters the Not Running state.
**Admit** - A process in the New state is added to list of processes ready to state, in Ready state
**Dispatch** - A process that is not currently running begins executing amd moves to Running state
**Suspend** - A running program pauses execution, for whatever reason, and moves to Not Running state
**Exit** - A running program finishes, reaches the ```exit```, and can be removed from list of processes.
**Block** - A running program requests a resource, does not get it right away, cannot proceed
**Unblock** - A program, currently blocked, receives the resource it was waiting for, it moves to Ready state.
**Reap** - A terminated program's return value is collected by a ```wait``` and its resources can be released

There are two additional "Exit" transitions that may happen but are not shown. In theory, a process that is in
Ready or Blocked state might transition directly to Terminate state. This can happen if process
is killed, by the user or by parent (parent can kill their children any time).

It may also happen that the system has a policy of killing all the children of a parent when parent dies.

## Swapping Processes to Disk

A process might be swapped out to disk rather than memory.

Memory can have multiple processses in it and if the executing process gets blocked, another can
be swapped into memory.

- Possible that user wants more processes running then can currently be accomodated in main memory.
- Problem is not PCBs that are small but the stack and heap space allocated to the running program can be very large

- A first solution is to not allow starting porgrams when there is not free space in main memory.
Downfall: - Programs do not declare in advance how much memory will be used or will need.
- User will not be happy since opening stuff will say insufficient memory. 

- Another solution: buy more Ram. However we get larger processes when the size of memory increases

- With no place to put them, we have to put the processes on disk, this is called **swapping**.
- When demands for memory exceed available memory, some processes will be moved to disk storage
to make room for other processses. 

- Expensive operation: swapping a process to disk might transfer several hundred MB of data. Then
when we need to load it back to memory. Done only when necessary.

- We need new state swapped because we do not want to spend more time swapping the processs in and out
of memory than necessary.

- We will only swap a process to disk if it is blocked.

## Seven-State Model

Two Problems Solved:
1) What if all processes are ready but there is not enough memory space?

2) What if the event the blocked process was awaiting has taken placed and the process could
proceed? How can we tell if swapped processes had their events occur?

Solution: Split the swapped state in two: Ready/swapped (ready to run, and currently not in memorY)
and blocked/swapped (not ready to run, and currently not in memory). That gives us the final
seven-state model.

- Admit transition is modified to show that by default the new process does not start in main memory. Two
new transitions, Swap In and Swap out, are added to show a process being loaded into main memory and written
out to disk respectively. 

- There are additional "Exit" transitions that may happen but are not shown.
- Process is killed -> regardless in memory or disk -> move to Terminated.

## Preview of Scheduling

- Processes represented by their PCB are mainted in a data structure; typically a linked list
or a queue of some sort.
- It does not make sense to have all processes in a single linked list that we would have
to iterate over. If there are 200 processses and then next ready one is in 137 then it is
logical to take out non-ready processes from list.

- Where doe blocked processes go? This will be talked about scheduling. It's convenient
for OS to keep track of what processes are in which state separetly. 

- If a process is waiting for a disk operation, when the disk becomes available, it would
be convenient to know quickly what process(es) are waiting for the disk.

- A common way of looking at the way processes move around is in a queueing diagram.

- Process initially goes into ready queue until it is selected to run, then it is executed
on cPU. 

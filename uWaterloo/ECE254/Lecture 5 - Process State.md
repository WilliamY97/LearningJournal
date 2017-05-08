# Lecture 5 - Process State

The OS is responsible for determining which programs run when and how to allocate resources.
The current state of the process is therefore important information. To maintain the state of the
process the PCB has a variable, but we will think about this as a finite state machine (FSM): there
are limited number of states and defined transitions between them.

## The Two-State Model

- Either a process is executing, or it is not. Two states:

1. **Running**: Actively executing right now
2. **Not Running**: Not currently executing


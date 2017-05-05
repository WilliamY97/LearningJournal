# ECE224

## Introduction to Embedded Systems

Embedded System: Special purpose computer system designd to perform a task without user's knowledge of its existence. The user may
provide input to embedded system via controls and sensors but the user need not be aware of the presence of the system.

## Embedded System Design

- Simple embedded systems are constructed out of electronics w/o processor/software, however
there will be state.

- Complex embedded systems incorporate one or more processors with sophisticated development control
software

Hardware / Software Codesign: Term given to task of simulatenously designing hardware/software components of a combined
hardware/software system.

## Why is Embedded System Design Challenging?

- Multidisciplinary design problems
- Complex Device Interactions
- Unpredicatable external environment

- Security/reliability are very important

## Embedded Systems and Real-time

Real-time System: Correctness of a result depends on time which it is delivered

Soft real-time: Timing violation leads to degradation in the usefulness of the
embedded system

Hard real-time: A timing violation leads to total system failure

Real-time requirements typically emerge from control constraints:

Ex. system must send a command to an actuator 100 times a second

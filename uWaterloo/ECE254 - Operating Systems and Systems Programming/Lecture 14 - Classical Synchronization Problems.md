# Lecture 14 - Classical Synchronization Problems

## Classical Synchronization Problems

Various operating systems textbooks provide a few classical problems in operating systems.
These standard problems are used to test any newly-proposed synchronization or coordination scheme.
The solutions make use of semaphores as the basis for mutual exclusion.

Three types of problems:
1. The producer-consumer problem
2. The readers-writers problem
3. Dining Philosophers Problem

## The Producer-Consumer Problem

Most common sync problem is the Producer-Consumer problem, also known as the bounded-
buffer-problem. Two processes share a common buffer that is of fixed size. One process
is the producer - it generates data and puts it in the buffer. The other is the consumer:
it takes data out of the buffer. This problem can be generalized to have p producers and c
consumers, but for the sake of keep the explanation simple, we have one of each.

## Rules

- It is not possible to write into a buffer that is already full
- If the buffer has capacity N and there are N items in it, the producer cannot
write into the buffer and must wait until there is space
- It is not possible to read from an empty buffer - if zero elements, the consumer
cannot read from the buffer and must wait until something in there.

## How to Keep Track of Buffer?
To keep track of the number of items in the buffer, we use a variable ```count```. This
is a variable shared between more than one thread, and therefore access to this should
be controlled with mutual exclusion. Let us assume the max number of elements in buffer
is defined as ```BUFFER_SIZE```.

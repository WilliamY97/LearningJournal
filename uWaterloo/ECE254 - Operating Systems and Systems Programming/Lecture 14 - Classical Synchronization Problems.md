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

### Rules

- It is not possible to write into a buffer that is already full
- If the buffer has capacity N and there are N items in it, the producer cannot
write into the buffer and must wait until there is space
- It is not possible to read from an empty buffer - if zero elements, the consumer
cannot read from the buffer and must wait until something in there.

### How to Keep Track of Buffer?
To keep track of the number of items in the buffer, we use a variable ```count```. This
is a variable shared between more than one thread, and therefore access to this should
be controlled with mutual exclusion. Let us assume the max number of elements in buffer
is defined as ```BUFFER_SIZE```.

### Busy-Waiting Solution

If busy-waiting is permitted, we do not care if we are wasting CPU time, we can get away from
one mutex which we can call ```mutex```. Each of the producer/consumer threads very likely run
in an infinite loop on their own, but code below explains one iteration.

```
Producer
1. [produce item]
2. added = false
3. while added is false
4. wait( mutex )
5. if count < BUFFER_SIZE
6. [add item to buffer]
7. count++
8. added = true
9. end if
10. signal( mutex )
11. end while

Consumer
1. removed = false
2. while removed is false
3. wait( mutex )
4. if count > 0
5. [remove item from buffer]
6. count--
7. removed = true
8. end if
9. signal( mutex )
10. end while
11. [consume item]
```

While this accomplishes what we want, it's not efficient. With a third rule where we sa
to avoid busy-waiting. Thus when the producer is waiting for space it will be blocked and
just as the consumer will be when the consumer is waiting for an element.

To accomplish this, we will need two general semaphores, each with maximum value of
BUFFER_SIZE. The first is called ```items:``` it starts at 0 and represents how many spaces
in the buffer are full.

The second is the mirror image ```spaces``` it starts at BUFFER_SIZE and represents the # of
spaces in the buffer that are currently empty.

```
Producer
1. [produce item]
2. wait( spaces )
3. [add item to buffer]
4. signal( items )

Consumer
1. wait( items )
2. [remove item from buffer]
3. signal( spaces )
4. [consume item]
```

The producer can continue to produce items until the buffer is full and the consumer can
continue to consumer items until the buffer is empty. This works okay given that:
1. The actions of adding an item to the buffer and removing an item form the buffer add
to and remove from the "next" space;
2. That there is exactly one producer and one consumer in the system. If we have two
producers, for example, they might be trying to write into the same space at the same time,
and this would be a problem.

To generalize this solution to allow multiple producers / consumers, what we need to do is
add another binary semaphore, ```mutex``` (initialized to 1), effectively combining the
previous solution with one before it.

```
Producer
1. [produce item]
2. wait( spaces )
3. wait( mutex )
4. [add item to buffer]
5. signal( mutex )
6. signal( items )

Consumer
1. wait( items )
2. wait( mutex )
3. [remove item from buffer]
4. signal( mutex )
5. signal( spaces )
6. [consume item]
```

### Issues

- In synch parrtern from earlier, we mentioned the possibility of deadlock: all threads
getting stuck. The hint that there is a problem is one ```wait``` statement inside another.

Not always the case but the nested wait alarms us that there might be a problem.

### Analysis

Reading the code above, you should be able to reason out that this solution will not get stuck.
You may choose a strategy along the lines of proof by contradiction and tyr to come up with
a scenario that leads to deadlock. This is not a substitute to mathematical proof.

Consider Alternative Solution:

```
Producer
1. [produce item]
2. wait( mutex )
3. wait( spaces )
4. [add item to buffer]
5. signal( items )
6. signal( mutex )

Consumer
1. wait( mutex )
2. wait( items )
3. [remove item from buffer]
4. signal( spaces )
5. signal( mutex )
6. [consume item]
```
### Analysis

This solution is like the one we are certain works, except the order of ```wait``` has been
swapped. It does have the deadlock problem. If buffer empty, and consumer thread runs first, it
will wait on the ```mutex```, be allowed to proceed, and then will be blocked on ```items```
because the buffer is initially empty. The thread is blocked.

When the producer thread runs, it waits on ```mutex``` and cannot proceed because the consumer
thread is in the critical section. The producer is blocked and can never produce any items.
Thus we have a deadlock. This can occur any time the buffer is empty.

## The Readers-Writers Porblem

This is about concurrent reading and modification of a data structure or record by more than
one thread. A writer will modify the data; a reader will read it only without modification.
Unlike the producer-consumer problem, some concurrency is allowed:

1. Any number of readers may be in the critical section simultaneously
2. Only one writer may be in the critical section (and when it is, no readers are allowed)

### Summary

A writer cannot enter the critical section while any other thread (reader/writer) is
there. While a writer is in the critical section, neither readers nor writers may enter.

This is similar to general mutual exclusion problem and the producer-consumer problem.
In the reader-writers problem, readers do not modify the data (consumers do take things
out of the buffer, modifying it).

If any thread could read or write the shared data structure, we would have to use the
general mutual exclusion solution. Although it would be a serious performance reduction
versus allowing multiple readers concurrently.

### Analysis

Let us keep track of the number of readers at any given time with a variable ```readers```

We will need a way of protecting this variable form concurrent modifications, so there
will have to be binary sempahore ```mutex```. We will also need another semaphore
```roomEmpty```, as a way of indicating that the room is empty.

A writer has to wait for the room to be empty before it can enter. This solution is from:

```
Writer
1. wait( roomEmpty )
2. [write data]
3. signal( roomEmpty )

Reader
1. wait( mutex )
2. readers++
3. if readers == 1
4. wait( roomEmpty )
5. end if
6. signal( mutex )
7. [read data]
8. wait( mutex )
9. readers--
10. if readers == 0
11. signal( roomEmpty )
12. end if
13. signal( mutex )
```

The writer may only enter into the critical if the room is empty. When it has finished,
it signals that the room is empty. The writer can be certain that when it exits the
critical section that there are no other threads in the room, because no thread
may enter the room while the writer was there.

The first reader that arrives encounters the situation that the room is empty, so it
locks the room. Writers can't then enter the room. Additional readers do not check if
roomy is empty, they just proceed to enter. When the last reader leaves hte room, it signals
the room is empty. This pattern is called the light switch as the first in turns on lights
and last out turns off lights.

### Concern of Reader

The reader code has that situation that makes us concerned about the possibility of deadlock: a
wait on ```roomEmpty``` inside a critical section by ```mutex```. With a bit of reasoning, we
can convince ourselves there is no risk. Deadlock is not a problem.

### Second Problem

Suppose some readers are in the room, and a writer arrives. Writer must wait until
all the readers have left the room. When each of the readers is finished, it exits
the room. In the meantime, more readers arrive and enter hte room.

Even though each reader is in the room for a finite amount of time, there is never
a moment when the room has no readers in it. This undesirable situation is not
deadlock, because the reader threads are not stuck, but the writer (and any subsequent
writers) are going to wait forever. This is a situation called ```starvation```:
a thread never get a chance to run.

It must not be possible for a thread requiring access to the critical section to be delayed
indefinitely. Tis problem is just as bad as deadlock in that if it is discovered, it eliminates
a proposed solution as an acceptable option, even though starvation might only be an unlikely
event. We must thus improve solution so writer never starves.

### Solution to Starving Consumers


# Lecture 15 - Deadlock

Definition - The permanent blocking of a set of processes that either compete for system resources or communicate with each other.

A set of processes is deadlocked when each process in the set is blocked on some event that can only be triggered by another blocked
process in the set. In this case it is permanent, because none of the events can take place.

A deadlock involves some conflicting needs for resources by two or more processes.

It occurs when everyone tries to do the same thing at the same time.

## Deadlock Occurence

For deadlock to occur, we do not have to have symmetric processes trying to do the same thing at the
same time.

## Fatal Region

The area of the diagram where it says "Deadlock Inevitable" is known as the ```fatal region```. The existence of a fatal region means that
deadlock is inevitable (will eventually happen), but any particular execution of the program may or may not result in deadlock.

The joint progress diagram works well when there are two threads sharing resources, but for a situation of n processes sharing resources, an n-dimensional diagram would be needed. For n>=4, we can't represent that with a 2D surface.

## Reusable and Consumable Resources

Deadlock takes place when two processes/threads are competing for resources. We can classify a resource as *resusable* or *consumable*.
A reusable resource can be used by one process at a time, and is not depleted by that use. A process may lock the resource, make use of it
and then release it such that other processes may acquire it. Processors, memory, files, and semaphores are all examples of reusable resources. If process P gets resource A and then releases it, process Q can acquire it. Thus, the example above involving P and Q is a
deadlock involving reusable resources.

A consumable resource is one that is created and destroyed upon consumption. If the user presses the "Z" key on the keyboard, this generates an interrupt and produces the "Z" character in a buffer. A process takes the input and consumes the character (ex. vi editor
window) and it is unavailable to other processes. Other things that are consumable resources, but in theory could be waiting to receive
a message, if it is a blocking receive, and no process can send a message (because they are all waiting for some other process to send first).

## Conditions for Deadlock

When a disaster happens, it is typically a result of a chain of things going wrong. If any one of those things did not happen,
the disaster would be averted. This is referred to as "breaking the chain". There are four conditions for deadlock:

1. **Mutual Exclusion**: A resource belongs to, at most, one process at a time.
2. **Hold-and-Wait**: A process that is currently holding some resources may request additional resources and may be forced
to wait for them.
3. **No Preemption**: A resource cannot be "taken" from the process that holds it; only the process currently holding that resource
may release it.
4. **Circular-Wait**: A cycle in the resource allocation graph.

If the first three conditions are true, deadlock is possible, but deadlock will only happen if the fourth condition is fulfilled. A
resource allocation graph is a directed graph that tells us the state of the system by representing the processes, the resources, and which resources are held by which processes.

## Dealing with Deadlock

There are four basic approaches to dealing with deadlock, each of which we will examine in turn.

1. Ignore it
2. Deadlock prevention
3. Deadlock avoidance
4. Deadlock detection

## Deadlock Option 1: Ignore It

Prevent deadlock from being possible. The first three conditions for deadlock (mutual exclusion, hold and wait, and no preemption) are
all necessary for deadlock to be possible. If we eliminate one of theses three pillars, deadlock is not possible and it is prevented from happening.

## Deadlock Option 2: Deadlock Prevention

This approach is a way of preventing a deadlock from being possible. The first three conditions for deadlock (mutual exclusion, hold
and wait, and no preemption) are all necessary for deadlock to be possible. If we eliminate one of these three pillars, deadlock is
not possible and it is prevented from happening.

**Mutual Exclusion** - This pillar cannot, generally speaking, be disallowed. The purpose of mutual exclusion is to prevent errors like
inconsistent state or crashes. Getting rid of mutual exclusion to rule out the possibility of deadlock is a cure that is worse.

**Hold and Wait** - To prevent this, we need to make sure that when a process requests a resource, it does not have any other resource.

One plausible solution is that the process must request all resources at the beginning of the program.

**No Preemption** - If we violate this then that means we do have premption aka forcible removal of resources from a process.




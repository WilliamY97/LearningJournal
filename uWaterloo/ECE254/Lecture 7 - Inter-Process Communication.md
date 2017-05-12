## Inter-Process Communication (IPC)

When two or more processes on the same system would like to co-ordinate or exchange data the mechanism for doing so is called
*interprocess communication*, aka IPC. If a process shares data with another process in the system, the operating system will
provide some facilities to make this possible.

The motivations for inter-process communication are fairly obvious - examples include breaking a lrage tasks into smaller subtasks,
allowing multiple users to edit the same data, and system modularity.

Before proceeding, we need to define some idea about what communication is: transfer of data from one process to another.

Data being transferred is typically referred to as the *message*. The process sending that message is the *sender* and
the process receiving it will be the *receiver*.

Processes involved must have some agreement on what data a message should contain, and way the data is formatted. Though
there may be defined standards e.g. transferring data formatted in XML, for the message content, the processes themselves
would have to be aware of the fact the message is in XML format.

How this agreement is reached tends to fall outside the purview of the operating system; maybe authors agree in a meeting
or the sender publishes its format online and the authors agree in a meeting or the sender publishes its format online and
the author of the receiver program writes her code to accommodate that.

Sending and receiving of messages may be either synchronous or asynchronous. 

If sending is synchronous, the sender sends the message and then is blocked from proceeding until the message is received. If sending is asynchronous, the sender can post the message and then carry on execution.

If receiving is synchronous, the receiver is blocked until it receives the message. If receiving is asynchronous, the
receiver is notified there is no message available and continues execution. Thus there are four combinations.

1. Synchronous send, synchronous receive: The sender is blocked until the receiver collects the message; the receiver
waits for a message and is blocked until it arrives.

2. Synchronous send, asynchronous receive: The sender is blocked when the message is sent, but the receiver will continue
whether or not a message is available. This is uncommon.

3. Asynchronous send, synchronous receive: Sender continues execution when the message is sent, but receiver will wait
until the message is received before it can continue. This is the most common configuration; usually the receiver needs
a message to continue.

4. Asynchronous send, Asynchronous receive: Sender can continue as soon as it sends the message, and the receiver will
check for a message but will continue whether or not the message is available.

Common in async receive for reciever to send back another message confirming receipt of the message. When that happens
just reverse labels: receiver of initial message is sender of acknowledgement.

## Implementation Strategies

Three approaches we consider on how to accomplish IPC:

1. Shared memory
2. The file system
3. Message passing

All of these methods are quite common and a system can easily implement them all. There is no single option that is optimal
in every situation, but each method has some areas of strength and weakness.

## Shared Memory

Conceptually, the idea of shared memory is very simple. A particular region of memory is designated as being shared between
multiple processes, all of whom may read and write to that location. To share an area of memory, the OS must be notified.

A region of memory is associated with exactly one process (its owner) and that process may read and write that location, but
other processes may not. If another tries to do so, the OS will stop it and make an error. If a process wants to designate
memory as shared, it tells operating system iti s okay fro the other process to have access to that area.

OS needs to know the memory is referenced by two processes: if the first one terminates and is reaped, the memory may still
be in use by the second process, so that previously-shared region should not be considered free as long as the second process
is still using it. Once the area of memory is shared, when either process attempts to access it, it is just a normal memory
access. The kernel is only involved in the setup and cleanup of that shared area.

Shared memory is created in block for the process that creates it. Process A will request the memory from operating system
and then ask the OS to consider a particular block A already owns to be shared.

When a section of memory is shared, there exists possibility that one process will overwrite another's changes. To prevent
this sort of problem, we will need a mechanism for co-ordination...

## File System

Another way to communicate is through file system. Unlike share memory, messages stored in the file system will be persistent
and survive a reboot. Also useable when the sender and receiver know nothing about one another (and the programmer knows nothing
about proper IPC mechanisms).

Rather than have OS get involved, the producer may write to a file in an agreed upon location and consumer may read from location.
The OS is involved in its role in file creation and manipulation (also permissions for read/write).

If one file is being used then we still have problem with co-ordination: make sure one process does not overwrite the changes
of another. We can get around this, however, by using multiple files with unique IDs.

Consider when producer generates XML data and writes to import/ directory. Consumer scans directory and when it finds it, reads
the file and imports the data contained therein. The imported data is then shown in the program. When one file writes and another
reads, there is no possibility for overwriting of data. As long as sender chooses distinct file names, it will not overwrite
a message if a second message is created before the receive picks up the first.

## Message Passing

A service provided by the operating system where the sender will give message to OS and ask for it to be delivered to a recipient.
There are two basic operations: sending and receiving. Messages can be of fixed or variable size.

Under *direct communication*, each process that wants to communicate needs to name the recipient or sender of
communication, makingthe send/receive functions:

```send(A, message)``` - Send a message to process A
```receive(B, message)``` - Receive a message from process B

**Symmetric Addressing**: The sender and receiver have to know one another to communicate

This deviates from the example of postal mail: receiving an item does not require foreknowledge of the sender.

**Asymmetric Addressing**: The sender names the recipient, but the receiver can pick up items from anyone. System
calls for the scheme are:

```send(A, message)``` - Send a message to Process A
```receive(id, message)``` - Receieve a message from any process; the variable id is set to the sender

- In either case we have to know some identifier for the other processes. Not very flexile; if we want to replace
process B with some alternative sftware, do we have to change the identifier in A, recompile it, and reinstall it?

**Indirect Communication** - Where messages are sent to mailboxes. This makes our send and receive functions:

```send(M, message)``` - Send a message to mailbox M.
```receive(M, message)``` - Receive a message from mailbox M

A mailbox may belong specifically to one process or may be set up by the operating system. If mailbox belongs
to the process, then anyone can send to this mailbox, but only the owning process may receive messages from
that mailbox. If the owner process has not started / terminated, attempt to send to mailbox will be error
for sender.

If the mailbox is owned by OS, it is persistent/independent of any particular process. When we used direct
communication, the communication relationship is 1:1 - one sender / receiver. There is no reason that an
OS mailbox can't belong to more than one process. If mailbox M belongs to the OS and processes P1 and P2
have access to it, which process gets message sent to mailbox?

Two ways to deal with this problem:

1. OS should allow only one process at a time to pick up items from the mailbox, thus preventing the problem altogether.

2. The other solution is that the OS may have some scheme: whichever process gets there first, alternation (take turns)
or any other system of deciding whose turn it is.

## Message Queues

Thus far we have dealt with messages one at a time: if sender wants to send a second message before first message
is received, the sender will have three choices, regardless of whether the communication is synchronous:

1. Wait for the last message to be picked up (block)
2. Overwrite the last message (seomtimes this is what you want)
3. Discard the current message (let the old one remain)

A message queue may alleviate the problem or just "kick the can down the road". If a queue exists, when sending
a message, that message is put in queue and when receiving message, the first message is taken. If queue is infinite
size, then the problem can be ignored. If the queue is fixed size, then the problem is put off but not solved:
the sender can keep adding messages to queue until queue is full. If queue is full: sender must choose to block,
overwrite, or discard.

## Unix Pipes

In UNIX, we can create a ```pipe``` to set up communication between producer and consumer. The producer writes in
one end of pipe and the consumer receives it on the other. This is unidirectional, so if you want bidirectional
communication, two pipes needed. The UNIX method for creating a pipe is ```pipe``` and is constructed with the
```pipe( int fileDescriptors[])``` where ```fileDescriptors[0]``` is the read-end and ```fileDescriptors[1]```
is the write-end.

```fileDescriptors``` means that UNIX thinks of pipe as a file (UNIX thinks everything is file) even though it is
in memory.

The pipe itself is a block of main memory that is interpreted as a circular queue, and each entry in the queue is
fixed in size and usually one character. The sender may place message in queue as small chunks, but the receiver gets
data one character at a time. Thus, sender and receiver need to know when the message is finished. This may be
through the use of a designated termination character (e.g., the line feed or null character), or the message
may begin with an explicit value of the number of characters the message will be. 

A UNIX pipe may be stored on disk. When this happens, we call it a **named pipe**. Unless we make it a named pipe, a pipe
exists only as long as the processes are communicating. Regular pipes depend on file descriptors, so if a parent-child
relationship is required to get the descriptors from one process to another. The named pipe, however, might be used
by any process and will persist even after the creating process has terminated. 

Another bonus of named pipes is that they are bidirectional, so we do not need two pipes for communication to go in
both directions. With that said, communication can only go in one direction at a time; if concurrent communication
is required, a second pipe is needed after all.

A command like ```cat fork.c | less``` creates a pipe that takes the output of the ```cat``` program and delivers it as
input to the program ```less``` which allows for scrolling and pagination of that data.

## UNIX Pipes: Code Example



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




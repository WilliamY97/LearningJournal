# The Process in UNIX

- We saw in UNIX that a process can create another process. The creating process is the
parent and the newly-created processes are its children. Every process has a parent
stretching back to the **init** process at root of tree.

Each process that has a unique identifier in its process control block (PCB), and
in UNIX we call this the **pid** (process ID).

Users will not need to know or think about the ID of a process except when trying to
terminate one that's gotten stuck (kill -9 24601). The **init** gets pid of 1.

Don't try to kill **init**. It likely stops attempt, but if it goes through then you
might need to reboot computer or cause a crash.

In a UNIX system (Ex. MAC OS), we can obtain a list of processes any time with the
**ps** command.

Each user when logging in, spawns a **login** process.

The user's shell (almost always bash, Bourne Again Shell) is then spawned from **login**.
That shell provides the command line interface where the user can enter a command.

When a command is issued, like **ls** or **top** (table of processes), the new process is
created and the shell will **wait** on that process to finish (in the case of **ls**) or
for the user to tell it to exit(**top**); Then the control goes back to the shell and you
get presented with the prompt again.

This would seem kind of limiting - do I have to log in to the system in a second terminal
window to run two things at a time? The answer is no, and there are two ways to get around it.

The first thing we can do is tell the shell we want the task to run in the background. To do that
add to the command the **&** symbol, like so:

```gc fork.c &```

This will return control immediately to shell (won't wait for gcc command to finish). You may see
process ID like 34429 showing that the child has been created. When the process is finished, there is another
update, looking something like:

```Done gcc fork.c```

Notably, any console output that the ```gc``` command would generate will still appear on the console where the
background task was created. Maybe you want that but maybe you want to put the output in a log file with a command like
```cat fork.c > logfile.txt &```.

The semantics of ```&``` are not just saying "run in background" it is actually the parent process (the shell) disowning
its child (the ```cat``` or ```gc``` process) so that process will get adopted by ```init``` and can run to completion even
if the user logs out.

A common example of a command I use involving the ```&```:

```sudo service xyz start &```

This will (with super user permissions aka sudo) start up the service ```xyz``` but return control to the console so I don't have
to wait for the ```xyz``` service to be started to enter my next command. This is good, because the next thing I'd like to is
```tail -f /var/log/xyz/console.log``` which will allow me to watch the console log of the xyz as it starts up to see if there
are any errors.

Other way of getting something to run in the background is to use ```screen``` command. Running something in the background isn't
great for interactive processes. Suppose you are working on some code in ```vi``` and you would like to pause that for a minute
and write an e-mail (with ```pine```). A approach would be to save and exit ```vi``` and open up ```pine```. The other would
be to start up each of these in ```screen``` and switch between them.

## Spawning Child Processes

When a process spawns a child, the child will need resources (memory, files, etc.). The child may request them from the OS directly
or the parent can give some of its resources to the child. The parent may partition resources amongst children or allow children
to share them instead.

Restricting a child process to only be able to use some subset of its parent resources means that a process cannot overload the
system by spawning too many children.

At time of initialization the parent can give child some data. When a new process is created, the child process may be a duplicate
of the parent process, or it may have a new program loaded into it.

## Show Me The Code!

Workflow in UNIX is as follows. First, parent spawns the child process with the ```fork``` system call. If it is interested in
waiting for the child process to finish, it will use the system call ```wait```, in which case the parent will be awaiting the
completion of the child process. When child process is finished, it returns a value with the ```exit``` system call.

The parent process will then get this as the return value of ```wait``` call and may proceed.

What does ```fork``` do? It creates a new process; it makes a copy of itself. The parent and child continue execution after
```fork``` statement. If ```fork``` returns a negative number, the ```fork``` failed. If it returns 0 then the process that
got 0 back is the child. If it returns positive value, that is the process ID of the child.

After the ```fork```, one of the processes may use the ```exec``` system call, or one of its variants, to replace its memory
space with a new program. No rule that says this needs to happen; a child can continue to be a clone of its parent if it wishes.
The ```exec``` invocation loads the binary file into memory and starts execution.

At this point, the programs can go their seperate ways, or the parent might want to wait for the child to finish. The parent is
then blocked, waiting for the child process to execute.

Actual C-Code Example:

```
int main()
{
  pid_t pid;
  int childStatus;
  /* fork a child process */
  pid = fork();
  if (pid < 0) {
    /* error occurred */
    fprintf(stderr, "Fork Failed");
    return 1;
  } 
  else if (pid == 0) {
    /* child process */
    execlp("/bin/ls","ls",NULL);
  } 
  else {
    /* parent process */
    /* parent will wait for the child to complete */
    wait(&childStatus);
    printf("Child Complete with status: %i \n", childStatus);
  }
return 0;
```

When executed, this code starts up and attempts to spawn a child process. Let us assume that the ```fork``` command succeeds and 
we do not enter the error block. After the fork there are now two processes at the statement ```if (pid<0)```. The child process
calls ```execlp```, replacing itself with the ```ls``` (list directory contents) command.

The parent process wil go the ```wait``` statement and wait for the child process to complete. The child process runs ```ls```,
listing the contents of the directory. Then it finishes. The parent process finally prints "Child complete" to console.

Thus the output is:

```
jz@Freyja:~/fork$ ./fork
fork fork.c
Child Complete with status: 0
jz@Freyja:~/fork$
```

What about termination? On the assumption that the process is terminating normally and not being killed, the
system call for that is ```exit```. Modify code above to fork off a child process that will exit “abnormally”
with an exit code of 1. The wait function also returns the process ID of the child so that the parent can identify
which of its children has terminated, though it is not used in this example.

```
int main()
{
pid_t pid;
int childStatus;
/* fork a child process */
pid = fork();
if (pid < 0) {
/* error occurred */
fprintf(stderr, "Fork Failed");
return 1;
} else if (pid == 0) {
/* child process */
exit( 1 );
} else {
/* parent process */
/* parent will wait for the child to complete */
wait(&childStatus);
printf("Child Complete with status: %i \n", childStatus);
}
return 0;
}
```
If the program itself has no explicit call to ```exit```, the ```return``` statement at the end of the ```main``` will have
the same effect.

## UNIX System V Process Management

Unix divides processes into two categories: system processes that run in kernal mode and user processes that run in user mode.
There are nin different states a process can be in:

1. User Running: Executing in user mode.
2. Kernel Running: Executing in kernel mode.
3. Ready to Run, in Memory: Ready to run; in memory.
4. Asleep in Memory: Blocked; in memory.
5. Ready to Run, Swapped: Ready to run; not in memory.
6. Sleeping, Swapped: Blocked; not in memory.
7. Preempted: Process is returning from kernel to user mode, but the kernel decides to run another process at this time.
8. Created: Newly created and not yet ready to run.
9. Zombie: Process is done, but the parent has not yet collected the return information.

Very like the sevenp-state model we saw earlier. The two major differences:

(1) The running in user mode vs. running in kernel mode
(2) The preempted state. It's like ready to run in memory, but the difference is how the process got to be in that state.

When a process is running in kernel mode as a result of system call, ex. when control is about to go back to the user
program, this is as good a time as any to swap to another process. So that would put the process in the preempted state
rather than ready to run, in memory. But these two states are really the same, logically.

## Process Creation

Process creation takes places when ```fork``` is called. When that happens, the OS takes the following steps:

1. Allocates slot in process table for new process
2. Assigns unique process ID to child process
3. Makes copy of process image of the parent, with exception of shared memory.
4. Increments counters for any files owned by the parent (shows additional process referencing those files)
5. The new process is in the state Ready to Run
6. A return value of 0 goes to child process, and unique process ID of child is returned to parent

All of above happens in kernel mode in the parent process. When it is done, the system will need to choose which process is gonna run:

1. Parent Process. The child is in the ready to run state.
2. Child Process. The parent is in the ready to run state.
3. Another Process. Both parent and child are in the ready to run state.

Seems strange that to spawn a process, the parent most make clone of self and continue from same point. Branching only if the
return value of the ID is tested.

## Fork Bomb

Call ```fork``` repeatedly until the number of processes spawned is too high for system to manage and it crashes/ or is so slow
that no useful work can get done. Two both call fork and so on causing 2^n invocations and this exponential growth crashes it.

A system configured to stop this may:
1. Limit total # of processes a user may create
2. Limit rate at which user may spawn a new process


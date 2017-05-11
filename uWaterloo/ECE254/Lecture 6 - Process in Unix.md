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
return
```

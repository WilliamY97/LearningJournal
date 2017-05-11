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


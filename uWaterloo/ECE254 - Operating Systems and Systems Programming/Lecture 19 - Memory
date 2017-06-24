# Lecture 19 - Memory

## Main Memory

In execution of program, CPU fetches instructions from memory, and decodes the instruction. It may be that the instruction
requires fetching of operands from memory. After the operation is completed, the result may be stored back in memory.

Ex. a single simple instruction like an addition could easily result in four memory accesses.

Executing a program therefore means spending a lot of time interacting with memory.

Like CPU, main memory is a resource that needs to be shared b/w multiple processes. The way programs are written, application developers
behave as if (1) main memory is unlimited, and (2) all of main memory is at the program's disposal.

Simple logic tells us that application developers are wrong: an infinite amount of data storage would req. an infinite amount of space.

One of the major objectives of the operating system is to manage shared resources, and that is exactly what main memory is.

## No Memory Management

Simplest way to manage memory is to not manage it at all. 

Problem: If two programs write to address 1024, then the second program will overwrite the first one's changes and it will probably
result in errors or a crash. If they know of each other, then the first program can use memory locations less than 2048 and the other can use
locations above 2048.

This level of execution gets more and more difficult as more and more programs are introduced to the system and is next to impossible if we
do not control (have the source code to) all the programs that are to execute concurrently.

**Solution**: On every process switch, save the entire contents of memory to disk, and restore
the memory contents of the next process to run.

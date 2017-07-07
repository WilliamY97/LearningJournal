# Lecture 21 - Memory Segmentation and Paging

## Memory Segmentation

- Although being repeatedly told that memory is a linear array of bytes, you have also
likely been told that there's the stack and the heap, libraries and instructions. Both
of these are true; they are simply views of memory at two different levels of abstraction.
Each of the elements such as the stack, the heap, the standard C library, etc known as
*segments*.

Rather than think about memory as a pure address, we can think of it as a tuple: given
that, we need an implementation to map these tuples into memory addresses. The mapping
has a segment table; each entry in the table contains two values: the base (starting
address of the segment) and the limit (the length of the segment). So there will be
some addition involved as well as a comparison to see if the address lies within that range.
As is typically the case, memory accesses are such a common operation that we will need another rescue
from hardware folks to make this not super slow.

With segmentation, memory need no longer be contiguous; we can allocated different parts of the
program in different segments; different segments can be located in different areas of memory.

## Paging

- Fixed and variable size both suffer from external/internal fragmentation. Let us divide
memory up into small, fied-size chunks of equal size, called *frames*. Each process's memory
is divided up into chunks the same size as a frame, called *pages*. Then a page can be assigned to
a frame. A frame may be empty or maye have exactly one page in it.

- When a process starts, it is loaded into memory, and has some initial memory requirements, so
it will require some number of pages. The number of pages can and will change over time as memory
is allocated and freed. A process may also be swapped out to disk, but to run it will need to be swapped
back in. Either way, a process will take up a certain number of pages in memory at any given time.

Pages provide the benefit of seperating the logical address from the physical address: programmers may pretend
the address space of the computer is 2^64 bytes rather than however many GB of memory are in the physical machine.

- Now we need a page table, to keep track of which tables are located where in memory. A list of
free frames is also necessary.

**Page Table:** Used to map logical memory to physical memory.

- For convenience, page size is usually a power of 2 (makes translating a logical address
into a tuple of the page number and offset easy.

- External fragmentation is eliminated as a problem in this scheme, because pages are all
the same size. That means compaction is also not an issue. It is therefore desirable to
avoid it entirely. We accept some internal fragmentation because a process gets a whole
page at a time.

- How about internal fragmentation? Not alot. If the memory required aligns perfectly with
a multiple of the page size, then no memory is wasted. If a new memory allocation comes in,
then a new page is allocated and added to the logical memory space of the process. The last
frame, however, may not be completely full. In the worst case scenario, a full page less one
byte is wasted. However, internal fragmentation of one page is not very much in the grand
scheme of things.

- How big should page sizes be? If they are smaller, then less memory is wasted in internal
fragmentation. However, having a large number of pages introduces a lot of overhead. The size
pages has tended to grow along with the size of main memory in computers. The key factor is actually
disk: the disk operates on a certain block size and it is most efficient for the size of a page
to be equal to a disk read/write size. That way when a page is to be swapped into or out of memory,
it can be done in a single disk read or write.

Now we finally have a good answer to why a developer can treat memory as if it is infinitely
large and unshared. The program is scattered across physical memory, but appears to the
developer and running application as if it is all contiguous.

- Also protection in this scheme because a programm cannot access any address outside of its
memory space. There is simply no way to make a memory request outside of the logical memory
space. No matter what address is generated, it could only be inside the page table, and the
page table has only entries of that process.

The operating system, however can manage memory of all processes so it will need another scheme.
The OS will operate on the *frame table*, a listing of all the frames, indicating which page
of which process a frame currently holds.

## Shared Pages

- Another benefit of paging is **sharing common code**. Users very often have multiple porgrams open
and sometimes they are duplicates. In a multiuser system, we can reduce memory consumption
if common parts of this program are shared between all instances of that program.

Other programs and code can easily be shared, such as compilers, libraries and operating system
utilities. In fact, any code can be shared as long as it is *reentrant* (also sometimes called
pure or stateless). That is code that does not change when it is executed. That means there is
no state maintained by the code.

## Page Table Structure

### Hierarchical Paging

- Rather than have a big table, we have multiple levels in the page table. This means the page
table can be broken up and need not be contiguous in memory. Suppose we have a two level system.
If the page number is *p*, the first *k* bits indicate the *outer page*. The outer page contains
some information about where the *inner pages* are. The remaining p-k bits identify the inner
page. After the inner page is identified, the displacement d is then calculated from the inner
page.

### Hashed Page Tables

Instead of the page table being an array of entries, turn it into a hash table. There is a hash
function to assign pages to "buckets" and each bucket is implemented as a linked list. Then
each element of the list is examined to find the matching page.

### Inverted Page Tables

For 64-bit computers, with 4 KB pages, the page table requires 2^52 entries, ad if an entry
is 8 bytes, then the table is over 30 million gigabytes. Unrealistic. Instead, we can have an
inverted page table: there is one entry per frame, rather than one entry per page. The entry
keeps track of the process and page number. This saves a huge amount of space (1 GB of ram).
The drawback is that it is no longer possible to find a physical page by looking at the
address; instead, we must search the entire inverted page table. Slow as this operation is; we can make it
faster via hardware.

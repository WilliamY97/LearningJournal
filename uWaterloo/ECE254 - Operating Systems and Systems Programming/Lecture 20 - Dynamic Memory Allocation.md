# Lecture 20 - Dynamic Memory Allocation

C works with memory at a lower level: to allocate a block of memory in C, there is
```malloc()``` and when finished, you return it with ```free()```. This level is a lot
closer to the way the operating system thinks about memory: just tell me how much
you need and tell me when you are finished with it.

When you call free(), it's just saying that the memory is free now. Sometimes you can
get away with dereferencing a pointer after it has been freed. AKA the original contents
are still there.

## Fixed Block Sizes

A way of allocating memory that is in fixed blocks. All blocks are allocated as the
same size. If a request comes in for 1 byte, 1 block is allocated. If a request is for
1.5 blocks, we still allocate 2 blocks.

- Memory is obviously wasted by doing this. Also known as *internal fragmentation* -
unused memory that is internal to a partition. This is obviously going to occur often
when fixed block sizes are used, and hte bigger each block is, the more memory will be
wasted in internal fragmentation.

**One Size of Blocks** - Treat blocks as nodes in linked list. Then when a block
is allocated we can remove the node from the list. When a block is freed, put a node with
that address into the linked list. If the list is empty, a memory request cannot be satisfied,
and null will be returned. We allocate thus in O(1) Time.

**Fixed Block Sizes, Multiple Size Options** - Have several different block sizes.
Unfortunately, fixed block sizes suffere from a lot of internal fragmentation. This may
be ok for embedded systems where simplicity/speed is more important than wasting memory.
Obvious that malloc() in C does not work like this. We need variable block size.

## Variable Block Sizes

Not that different from fixed sizes, we just take the size of blocks to the smallest they
can be. In a typical system with byte-addressable memory, in a way, the smallest block is
one byte. Now we have a different problem: keeping track of what is allocated and what is
free.

**Bitmaps** - Possible to divide memory into M units of n bits, and then to create a bit
array of size M storing the status of each of those units. If a bit m in M is 0, it means
that unit is unallocated; if it is 1 then that unit is allocated.

- Memory lost to overhead: 100/(n+1)% of the memory used

If a unit is 4 bytes, the bitmap is about 3% of the memory; if it is 16 bytes the bitmap
takes about 0.8% of memory. Finding a block of k bytes requires searching the bitmap for
a run of 8k/n zeros.

**Linked Lists** - The other approach, as in the case of fixed sizes blocks is to use
linked lists. The information of the linked list can be stored separately from all memory
allocation or as part of the block of memory. Either approach is workable.

Ex. When a memory request is allocated, the block is divided up. This may lead to a lot of
allocation and deallocation of memeoyr that leads to breaking up memory into smaller pieces.
They may be left small and spread out.

**Problem**: We may end up where there is a block of free memory available of size N, but
this request cannot be fulfilled because the memory is logically split up into smaller pieces.
To solve this we need to recombine the split blocks: also called **coalescence**.

**Coalescence**: Just the process of merging two or more free blocks into one larger block. It
also makes sense that diving memory should be a reversible operation. This solves the problem of
a block of N contiguous bytes being unable to be allocated. Coalescence can be done periodically
or whenver a block of memory is freed.

Coalescence makes it a good idea to maintain memory blocks in a doubly-linked list. Recall
that a linked list has "next" pointers connecting nodes and a double-linked list has a
next and previous pointers, to make it easier to traverse the list in both directions. When
the block is freed, it maye be in the middle of two free blocks, so it is convenient to
have previous and nextpointers so the adjacent sections can be merged efficiently.

**Where coalescence can't fix the issue**: The problem is that N free bytes exist but are
spread apart. When free memory is spread into tiny fragments, this is called **external
fragmentation**.

## External Fragmentation Reduction

One way to reduce external fragmentation is to increase internal fragmentation. When
a request for N bytes comes in and there is a block of N+k available, where k is very
small, it makes sense to allocate the whole N+k block for the request and just accept
that k bytes are lost to internal fragmentation. 

### Second Idea: Compaction or Relocation

Goal is to move allocated sections of memory next to one another in main memory, allowing
for a large contiguous block of free space. This is a very expensive operation; to do this
means stopping the whole world while it reorganizes the memory.

## Variable Allocation Strategies

Five strategies: first fit, next fit, best fit, worst fit, quick fit

As a performance optimization, we could have two linked lists: one for allocated memory
and one for unallocated memory. that way to find a free block we do not have to look
through the allocated blocks.

**First fit** - The strategy of first fit is to start looking at the beginning of memory
and check each block. If the block is of sufficient size, split it to allocate the memory,
and return the balance to the unallocated memory list. This algorithm has a runtime
of O(n) where n is the number of blocks. This algorithm is simple to implement.

**Best fit** - Instead of walking through the list and splitting up the first block equal
to or larger than N, we could instead try to make a more intelligent decision. Considering
all blocks, we choose the smallest block that is at least as big as N. This produces the
smallest remaining unallocated space at the end.

**Worst fit** - Leftover bits of memory are likely to be too small to be useful. Rather than
trying to find the smallest block that is of size N or greater, choose the largest block
of free memory. When the block is split, the remaining free block is, hopefully, large
enough to be useful

**Quick fit** - Though not a solution on its own, quick fit is an optimization. If memory
requests of a certain size are known to be common, it might be ideal to keep a seperate list of blocks
that are of perhaps 1-1.1 MB in size, so that if the request for 1 MB does come in, it can be satified
immediately and quickly.

## Choosing a Strategy

- Performance problems of worst fit can be fixed, of course, by keeping the memory blocks in a
max heap, but that still does not address the waste space problem. First (next) and best fit are
about equal in how well they utilize memory, but first fit tends to be faster. Even with optimization,
given x allocated blocks, another 0.5x blocks may be lost to fragmentation.

- First fit is the fastest and best algorithm. The next fit algorithm tends to do allocations at the
end of memory, so the largest block of free memory (typically at the end) is quickly broken up. On
the other hand, first fit tends to litter the beginning of memory with small fragments. Best fit
tends to produce free blocks that are too small to be useful.




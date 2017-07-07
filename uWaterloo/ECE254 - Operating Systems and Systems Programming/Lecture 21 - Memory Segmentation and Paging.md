# Lecture 21 - Memory Segmentation and Paging

## Memory Segmentation

- Although being repeatedly told that memory is a linear array of bytes, you have also
likely been told that there's the stack and the heap, libraries and instructions. Both
of these are true; they are simply views of memory at two different levels of abstraction.
Each of the elements such as the stack, the heap, the standard C library, etc known as
*segments*.


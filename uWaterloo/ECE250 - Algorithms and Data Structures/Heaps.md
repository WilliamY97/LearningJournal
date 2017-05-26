# Heaps

A heap is a typer of data structure. The benefit of them is that you can get the largest element from them in O(1) time.
This is much better than other data structures like an array where the operation is O(n) time. Extracting the largest element
from the heap takes O(logn) time.

These make a heap very good for implementing a priority queue. They also are used in the nlogn sorting algorithm, heap sort, which
works by repeating an extract of the largest element until we have emptied the heap.

# Intuitive View of Heap

A max heap can be viewed as a binary tree where each node has two or fewer children. The difference is that the key of each node
is greater than the keys of its child nodes. There are also min heaps which are the opposite of that.

NOTE: It is possible for some nodes in level 3 to be smaller than nodes on level 4 (if they're in different branches of the tree).

The heap is an almost complete binary tree and so all levels are filled except the one at the bottom. The bottom level gets filled
from left to right.

# Implementation of the Heap

You can implement a heap as an array. This array is essentially populated by reading the numbers in the tree, from left to right and from top to bottom.

The root is stored in index 1, and if a node is at index i then:

1. left child is index 2i
2. right child is index 2i + 1
3. parent has index floor(i/2)

For the heap array A, we also store two properties: A.length and A.heapsize (this is the number of elements are actually part of heap).
Even though array has a bunch of numbers, only the elements from A[1..A.heapsize] are actually part of the heap.

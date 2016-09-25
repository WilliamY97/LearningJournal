#Binary Tree

**Definition:** A data structure in which a record is linked to two successor records, usually referred to as the left branch
when greater and the right when less than the previous record.

##Implementation: LinkedList Vs. Array?

For a **binary tree** the answer is an array (if it's dynamic hopefully). Here is an analysis given that that **the tree is balanced**

**Query:** In a BST, nodes need to have pointers to left and right child and is also very common to have parent pointers. In an array
implementation, the "pointers" can simply be integer indexes into the array (this would mean the array would store **Node objects).

Thus looking up the parent and children of a node is constant since indexing into the array is constant. **O(1)**. A linked list
implementation would probably need to also store a reference to the position as to where their ancestors/children are, thus
requireing an **O(N)** pass through the list to get the desired references.

**Search:** Starting at the **root**, **array[0]**, searching would be an **O(n log n)** operation. Searching would just call/get the info
of the children per node, which is O(1) amount of work, roughly O(log N) times, thus **O(log N)** for search in an array.

A linked list would require an **O(N)** pass through the data to get the required left/right pinters, and can also be done in

**Insert:** Arrays would be similar to search, except would require additional O(1) constant time for pointer assignments. So O(log N) insert.

Linked-lists would also be similar to their search routine, except with an additional O(n) time for adjusting the pointers, so O(n log n)

**Delete:** Arrays would also be similar to search, except you could take more than a single O(log n) factor to delete, since you have to traverse back up the tree, but it still is O(log n).

Linked lists would too have the O(n log n) plus more O(n log n) for traversing up. So O(n log n) for linked lists as well.

**Conclusion:** Arrays are better and you also get the benefit of better caching than linked lists. Derivatives of a binary search tree
such as a **heap** are commonly represented as arrays.

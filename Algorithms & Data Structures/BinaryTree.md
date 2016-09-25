#Binary Tree

**Definition:** A data structure in which a record is linked to two successor records, usually referred to as the left branch
when greater and the right when less than the previous record.

##Implementation: LinkedList Vs. Array?

For a **binary tree* the answer is an array (if it's dynamic hopefully). Here is an analysis given that that **the tree is balanced**

**Query:** In a BST, nodes need to have pointers to left and right child and is also very common to have parent pointers. In an array
implementation, the "pointers" can simply be integer indexes into the array (this would mean the array would store **Node objects).

Thus looking up the parent and children of a node is constant since indexing into the array is constant. **O(1)**. A linked list
implementation would probably need to also store a reference to the position as to where their ancestors/children are, thus
requireing an **O(N)** pass through the list to get the desired references.


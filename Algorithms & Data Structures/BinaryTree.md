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

##Binary Search Trees

- Each node stores an item (k) of a dictionary

- Keys stored at nodes in the left subtree are less than or equal to k

- Keys stored at nodes in the right subtree are greater than (or equal) to k

##Searching in a BST

- compare k with T.key()
- if k < T.key(), search for k in T.left()
- otherwise, search for k in T.right()

##Pseudocode for BST Search

- Recursive
```
**
Search(T,k)
01 if T = NIL then return NIL
02 if k = T.key() then return T
03 if k < T.key()
04 then return Search(T.left(),k)
05 else return Search(T.right(),k)
**
```

- Iterative
```
Search(T,k)
01 x ← T
02 while x ≠ NIL and k ≠ x.key() do
03 if k < x.key()
04 then x ← x.left()
05 else x ← x.right()
06 return x
```

- Running time on tree of height h is O(h)

##BST Minimum (Maximum)

- Find the minimum key in a tree root at x (far left sub tree)

- Find the maximum key in a tree root at x (far right sub tree)

```
TreeMinimum(x)
01 while x.left() ≠ NIL do
02 x ← x.left()
03 return x
```

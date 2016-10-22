#Abstract Data Types

- Allows work to be broken into pieces that can be worked on independently without compromising correctness

- Serve as specifications of requirements for the building blocks of solutions to algorithmic problems

- Encapsulate **data structures** and algorithms that implement them

**ex.** A dictionary is a ADT that can be realized with different data structures such as Arrays, Binary Trees, Linked Lists, AVL Trees, Queues,
B-Trees, Stacks, Heaps, and Hash Tables

##Data Storage for ADT

- Data Storage can be classified as either Contiguous Storage / Node-based Storage

Examples: Contiguous Storage is the array / node-based is linked list

##Contiguous Storage
- An array stores n objects in a single contiguous space of memory
- Unfortunately, if more memory is required, a request for new memory usually
requires copying all information into the new memory.

##Node-Based Storage

- Node-based storage such as a linked list associates two pieces of data with each item
being stored:

The object itself, and a reference to the next item.

##Linked List ADT

- A data structure in which the objects are arranged in a linear order with dynamic
allocation

- Singly linked list - nodes(data, pointer) connected in a chain by links.

The before(p), insertBefore() commands take O(n) time and remove(p) takes O(n) time.

##Doubly Linked Lists

- To implement all of the linked list operations in constant time we use doubly linked lists
- A node of a doubly linekd list has a next and a prev link

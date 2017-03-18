# Linked Lists

![Reference Image](http://www.cs.usfca.edu/~srollins/courses/cs112-f08/web/notes/linkedlists/ll2.gif)

A linked list is a data structure that represents a sequence of nodes. In a singly linked list, each node points to the next node
in the linked list. A doubly linked list gives each node pointers to both the next node and the previous node.

**Unlike** an array... a linked list doesn't provide constant time access to a particular "index" within the list. This means that if you'd
like to find the Kth element in the lsit, you will need to iterate through K elements.

The benefit of a linked list is that you can add and remove items from the beginning of the list in constant time.

For specific applications, this can be useful.

If you make a really basic linked list with just a node class **watch out** as there may be a possibility that multiple objects need
a reference to the linked list, and then the head of the linked list changes... Some objects might still be pointing to the old head.

**Solution**: Implement a LinkedList class that wraps the Node class. This would essentially just have a single member variable:
the head **Node**. This would largely resolve the earlier issue. Remember that when you're discussing a linked list in an interview,
you must understand whether it is a singly linked list or a doubly linked list. 

## Deleting a Node from a Singly Linked List

- Given a node **N**, we find the previous node **prev** and set **prev.next** equal to **n.next**. If the list is doubly linked,
we must also update **n.next** to set **n.next.prev** equal to **n.prev**.

##The Runner Technique

- The runner technique is used in many linked list problems.

- You iterate through the linked list with two pointers simultaneously, with one ahead of the other. The "fast" node might be ahead by
a fixed amount, or it might be hopping multipled nodes for each one node that the "slow" node iterates through.

- For example, suppose you had a linked list a1 -> a2 -> ... -> an -> b1 -> b2 -> ... -> bn and you wanted to rearrange it to
a1 -> b1 -> a2 -> b2 -> ... -> an -> bn. You do not know the length of the linked list (but you do know that the length is an even
number)

- **Solution**: You could have one pointer p1 (the fast pointer) move every two elements for every one move that p2 makes. When p1 hits the end of the linked list, p2 will be at the midpoint. Then, move p1 back to the front and begin **weaving** the elements. On each
iteration, p2 selects an elements and inserts it after p1.

## Recursive Problems

- A number of linked list problems rely on recursion. If you're having trouble solving a linked list problem, you should explore if a
recursive approach will work. We won't go into depth on recursion, since a later chapter is devoted to it. 

- However note that recursive algorithms take at least O(n) space, where n is the depth of the recursive call. All recursive algorithms
can be implemented iteratively, although they may be much more complex. 

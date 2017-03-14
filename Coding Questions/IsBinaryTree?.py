"""
For the purposes of this challenge, we define a binary search tree to be a binary tree with the following ordering properties:

The  value of every node in a node's left subtree is less than the data value of that node.
The  value of every node in a node's right subtree is greater than the data value of that node.
Given the root node of a binary tree, can you determine if it's also a binary search tree?

Complete the function in your editor below, which has  parameter: a pointer to the root of a binary tree. It must return a boolean denoting whether or not the binary tree is a binary search tree. You may have to write one or more helper functions to complete this challenge.

Note: We do not consider a binary tree to be a binary search tree if it contains duplicate values.


Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def check_binary_search_tree_(root):
    lst = in_order(root)
    for i in range(1, len(lst)):
        if lst[i - 1] >= lst[i]:
            return False
    return True

def in_order(root, lst =[]):
    if root is None: return None
    in_order(root.left)
    lst.append(root.data)
    in_order(root.right)
    return lst

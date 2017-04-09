# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node)
or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.

SOLUTION: Unintuitive question. Start by recursing down to the leftmost node which will be the new head. Return upwards where
every node will move its right node to the left childs left node and move itself to be pointed to as its left child's right node.
Then snip its pointers to both its children. The weird part of this is that its parent will still point to it and its left child
will now point to it too. But moving up a node, its parent and the parent's right child will becomes its children.
"""

class Solution(object):
    def upsideDownBinaryTree(self, root):
        #if not root is to check if there is no
        #tree to begin with
        if not root or not root.left:
            return root
        
        newHead = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right
        root.left.right = root
        root.left = None
        root.right = None
        return newHead

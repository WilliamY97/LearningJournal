# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
SOLUTION: Switch place of left and right node. Call function recursively on left and right child. If hits null just return
"""

class Solution(object):
    def invertTree(self, root):
        if not root: return
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

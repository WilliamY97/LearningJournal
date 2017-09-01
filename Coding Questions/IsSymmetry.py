# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
For example, this binary tree [1,2,2,3,4,4,3] is symmetric.

SOLUTION: Recursive. Each left and right subtree should be a reflection of the other.

"""

class Solution(object):
    def isSymmetric(self, root):
        def IsSym(L,R):
            if not L and not R: return True
            if L and R and L.val == R.val:
                return IsSym(L.left,R.right) and IsSym(L.right,R.left)
            return False
        return IsSym(root,root)

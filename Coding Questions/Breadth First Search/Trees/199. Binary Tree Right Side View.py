# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        if root is None: return []
        res = []
        queue = [root]
        level = 0
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                
                if level == len(res):
                    res.append(node.val)
                
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
            level += 1
        return res

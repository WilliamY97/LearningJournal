# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        if not root: return []
        queue = [root]
        result = []
        
        while queue:
            size = len(queue)
            level = []
            for i in range(size):
                node = queue.pop(0)
                
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                level.append(node.val)
            result.insert(0,level)
        return result

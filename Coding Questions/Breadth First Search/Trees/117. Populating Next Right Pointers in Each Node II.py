class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None: return
        queue = [root]
        
        while queue:
            size = len(queue)
            last = None
            for i in range(size):
                node = queue.pop(0)
                if last:
                    last.next = node
                last = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            last.next = None
            

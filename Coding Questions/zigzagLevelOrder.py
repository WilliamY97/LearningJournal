def zigzagLevelOrder(self, root):
    if not root: return []
    res, temp, queue, flag = [], [], [root], 1
    while queue:
        for i in range(0,len(queue)):
            node = queue.pop(0)
            temp += [node.val]
            if node.left: queue +=[node.left]
            if node.right: queue +=[node.right]
        res+=[temp[::flag]]
        temp = []
        flag*= -1
    return res


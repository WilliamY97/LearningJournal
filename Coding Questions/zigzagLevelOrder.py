def zigzagLevelOrder(self, root):
    if not root: return []
    res, temp, stack, flag = [], [], [root], 1
    while stack:
        for i in range(0,len(stack)):
            node = stack.pop(0)
            temp += [node.val]
            if node.left: stack +=[node.left]
            if node.right: stack +=[node.right]
        res+=[temp[::flag]]
        temp = []
        flag*= -1
    return res


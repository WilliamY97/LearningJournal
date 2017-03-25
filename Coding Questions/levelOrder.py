def levelOrder(self, root):
    if not root: return []
    ans,level = [],[root]
    while level:
        ans.append([node.val for node in level])
        temp = []
        for n in level:
            temp.extend([n.left,n.right])
        level = []
        for leaf in temp:
            if leaf:
                level.append(leaf)
    return ans

def levelOrder2(self, root):
    if not root: return []
    ans,temp,stack = [],[],[root]
    while stack:
        for i in range(0,len(stack)):
            node = stack.pop(0)
            temp += [node.val]
            if node.left: stack += [node.left]
            if node.right: stack += [node.right]
        ans.append(temp)
        temp = []
    return ans


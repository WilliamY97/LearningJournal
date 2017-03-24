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


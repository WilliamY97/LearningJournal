# level is a list of the nodes in the current level.
# Keep appending a list of the values of these nodes to ans and then updating level with all the nodes in
# the next level (kids) until it reaches an empty level. Python's list comprehension makes it easier to deal
#  with many conditions in a concise manner.

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


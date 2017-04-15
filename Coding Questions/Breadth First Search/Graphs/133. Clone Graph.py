# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None: return None
        dic = {}
        dic[node] = UndirectedGraphNode(node.label)
        queue = [node]
        
        while queue:
            curr = queue.pop(0)
            for n in curr.neighbors:
                if n in dic:
                    dic[curr].neighbors.append(dic[n])
                else:
                    nCopy = UndirectedGraphNode(n.label)
                    dic[n] = nCopy
                    dic[curr].neighbors.append(nCopy)
                    queue.append(n)
        return dic[node]

class Solution(object):
    def validTree(self, n, edges):
        if len(edges) != n-1: return False
        neighbors = {i:[] for i in range(n)}
        
        for v,w in edges:
            neighbors[v].append(w)
            neighbors[w].append(v)
        queue = [0]
        while queue:
            queue.extend(neighbors.pop(queue.pop(0),[]))
        
        return not neighbors

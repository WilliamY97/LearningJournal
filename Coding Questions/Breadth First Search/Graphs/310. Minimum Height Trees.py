class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if edges == []:
            return [0]
        
        graph = {d: [] for d in range(n)}
        
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
                
        leaves = []
        
        for k in range(n):
            if len(graph[k]) == 1:
                leaves.append(k)
        
        while n > 2:
            n -= len(leaves)
            newleaves = []
            for l in leaves:
                curr = graph[l].pop()
                graph[curr].remove(l)
                if len(graph[curr]) == 1:
                    newleaves.append(curr)
            leaves = newleaves
                
        return leaves
                    

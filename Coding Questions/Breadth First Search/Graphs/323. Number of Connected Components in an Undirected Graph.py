class Solution(object):
    def countComponents(self, n, edges):
        neighbors = {i:[] for i in range(n)}
        for v,w in edges:
            neighbors[v].append(w)
            neighbors[w].append(v)
        
        visited = [False] * n
        res = 0
        
        for i in range(n):
            if visited[i] == False:
                res += 1
                queue = [i]
                visited[i] = True
                
                while queue:
                    cur = queue.pop(0)
                    
                    for k in neighbors[cur]:
                        if visited[k] == False:
                            queue.append(k)
                            visited[k] = True
        return res
                

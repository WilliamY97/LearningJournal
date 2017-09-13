class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = {d:[] for d in range(numCourses)}
        indegree = [0] * numCourses
        
        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a] +=1
        
        zero = []
        
        for i in range(len(indegree)):
            if indegree[i] == 0:
                zero.append(i)
        
        while zero:
            curr = zero.pop(0)
            for c in graph[curr]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    zero.append(c)
            del graph[curr]
        
        return len(graph) == 0

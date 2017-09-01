class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = {d:[] for d in range((numCourses))}
        indegrees = [0]*numCourses
        zeros = []
        result = []
        
        for a,b in prerequisites:
            graph[b].append(a)
            indegrees[a] += 1
        
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                zeros.append(i)
        
        while zeros:
            curr = zeros.pop()
            result.append(curr)
            for i in graph[curr]:
                indegrees[i] -= 1
                if indegrees[i] == 0:
                    zeros.append(i)
            del graph[curr]
        
        if len(graph) == 0: return result
        else: return []
        

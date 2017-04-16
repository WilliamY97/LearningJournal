class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        if n == 0: return 0
        
        res = 0
        queue = []
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    queue.append([i,j])
                    grid[i][j] = '0'
                    while queue:
                        [a,b] = queue.pop(0)

                        if a+1 < m and grid[a+1][b] == '1':
                            queue.append([a+1,b])
                            grid[a+1][b] = '0'
                        
                        if b+1 < n and grid[a][b+1] == '1':
                            queue.append([a,b+1])
                            grid[a][b+1] = '0'                        
                        
                        if a-1 >= 0 and grid[a-1][b] == '1':
                            queue.append([a-1,b])
                            grid[a-1][b] = '0'
                            
                        if b-1 >= 0 and grid[a][b-1] == '1':
                            queue.append([a,b-1])
                            grid[a][b-1] = '0'
                    res += 1
        return res
        

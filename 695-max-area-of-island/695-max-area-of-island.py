class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        Visited=set()
        row,coloum=len(grid),len(grid[0])
        max=0
        def dfs(i,j):
            if(i<0 or i==row or j<0 or j==coloum or grid[i][j]==0 or (i,j) in Visited):
                return 0
            Visited.add((i,j))
            return (1+dfs(i-1,j)+dfs(i+1,j)+dfs(i,j-1)+dfs(i,j+1))
        
        
        maxarea=0
        ls=[]
        for i in range(0,row):
            for j in range(0,coloum):
                a=dfs(i,j)
                if a>maxarea:
                    maxarea=a
        return maxarea  
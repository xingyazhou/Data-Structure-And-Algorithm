# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 19:45:43 2020

200. Number of Islands (Medium)

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

@author: xingya
"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        
        numOfisland = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == '1':
                    numOfisland += 1
                    self.dfs(grid, i,j)
                    
        return numOfisland
        
                    
    def dfs(self, grid, r, c):
        
        nr = len(grid)
        nc = len(grid[0])
        
        grid[r][c] = '0'
   
        if r-1 >= 0 and grid[r-1][c] == '1':
                self.dfs(grid, r-1,c)
                
        if r+1 < nr and grid[r+1][c] == '1':
                self.dfs(grid, r+1,c)
                
        if c-1 >= 0 and grid[r][c-1] == '1':
                self.dfs(grid, r,c-1)
                
        if c+1 < nc and grid[r][c+1] == '1':
                self.dfs(grid, r, c+1)
                         

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
s = Solution()
print(s.numIslands(grid))

# Output
# 3

"""
Runtime: 104 ms, faster than 99.38% of Python online submissions for Number of Islands.
Memory Usage: 19.9 MB, less than 56.10% of Python online submissions for Number of Islands.
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 20:13:01 2020

695. Max Area of Island (Medium)
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.

Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.

@author: xingya
"""

class Solution:
    def maxAreaOfIsland(self, grid):
        if len(grid) == 0:
            return 0
        
        r = len(grid)
        c = len(grid[0])
               
        maxArea = 0
        output = [0]
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                                 
                    self.dfs(grid, i, j, output)
                    maxArea = max(maxArea, output[0])        
                    output  = [0] 
                    
        return maxArea
                                
    def dfs(self, grid, i, j, output):
        r = len(grid)
        c = len(grid[0])
        
        grid[i][j] = 0        
        output[0] += 1

        
        if i-1 >= 0 and grid[i-1][j] == 1:         
            self.dfs(grid, i-1, j, output)
            
        if i+1 < r and grid[i+1][j] == 1:
            self.dfs(grid, i+1, j, output)
            
        if j-1 >= 0 and grid[i][j-1] == 1:
            self.dfs(grid, i, j-1, output)
            
        if j+1 < c and grid[i][j+1] == 1:
            self.dfs(grid, i, j+1, output)
        

class Test:
    def test(self):
        
        s = Solution()
        grid1 = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
        grid2 = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
                 [0,0,0,0,0,0,0,1,1,1,0,0,0],
                 [0,1,1,0,1,0,0,0,0,0,0,0,0],
                 [0,1,0,0,1,1,0,0,1,0,1,0,0],
                 [0,1,0,0,1,1,0,0,1,1,1,0,0],
                 [0,0,0,0,0,0,0,0,0,0,1,0,0],
                 [0,0,0,0,0,0,0,1,1,1,0,0,0],
                 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
        
        expected1 = 4
        expected2 = 6
        
        output1 = s.maxAreaOfIsland(grid1)
        output2 = s.maxAreaOfIsland(grid2)
        
        assert (output1 == expected1), "Wrong output, expected output is : 4"
        assert (output2 == expected2), "Wrong output, expected output is : 6"
        
        print(output1)
        print(output2)


t = Test()
t.test()

"""
Runtime: 96 ms, faster than 99.65% of Python online submissions for Max Area of Island.
Memory Usage: 15.2 MB, less than 40.28% of Python online submissions for Max Area of
"""

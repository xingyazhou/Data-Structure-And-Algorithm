# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 21:57:10 2020

64. Minimum Path Sum (Medium)
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

@author: xingya
"""

class Solution:
    def minPathSum(self, grid):
        if len(grid) == 0:
            return 0
        
        r = len(grid)
        c = len(grid[0])
                 
        for i in range(1, r):
            grid[i][0] = grid[i-1][0] + grid[i][0]
            
        for j in range(1, c):
            grid[0][j] = grid[0][j-1] + grid[0][j]
            
        for i in range(1,r):
            for j in range(1, c):
                grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
            
        return grid[-1][-1]
    
    
class Test():
    def testMinPathSum(self):
          
        grid = [[1,3,1],[1,5,1],[4,2,1]]
        expect_output = 7
        
        s = Solution()
        output = s.minPathSum(grid)
        
        print(output)
        assert (output == expect_output), "Wrong result, expected output is : 7"
        
t = Test()
t.testMinPathSum()


"""       
Runtime: 84 ms, faster than 99.86% of Python3 online submissions for Minimum Path Sum.
Memory Usage: 15.5 MB, less than 32.04% of Python3 online submissions for Minimum
"""
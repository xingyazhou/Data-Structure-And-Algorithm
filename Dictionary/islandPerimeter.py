# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 22:48:23 2020

463. Island Perimeter (Easy)

You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.


Example 1:

Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
Example 2:

Input: grid = [[1]]
Output: 4
Example 3:

Input: grid = [[1,0]]
Output: 4
 

Constraints:

row == grid.length
col == grid[i].length
1 <= row, col <= 100
grid[i][j] is 0 or 1.

@author: xingya
"""

import unittest

class Solution:
    def islandPerimeter(self, grid):
        
        if len(grid) == 0:
            return 0
        
        r = len(grid)
        c = len(grid[0])
        d = set()
        
        numOfland = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    numOfland += 1
                    d.add((i,j))
          
        numOfSharedEdge = 0
        for (i,j) in d:
            if (i+1,j) in d:
                numOfSharedEdge += 1
            if (i, j+1) in d:
                numOfSharedEdge += 1
  
        return numOfland * 4 - numOfSharedEdge * 2
        
class Test(unittest.TestCase):
    def testIslandPerimeter(self):
        print("\n\nTesting islandPerimeter ...\n")
        grid1 = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
        expected1 = 16
        
        grid2 = [[1,1], [1,1]]
        expected2 = 8
        
        s = Solution()
        output1 = s.islandPerimeter(grid1)
        output2 = s.islandPerimeter(grid2)
        
        assert output1 == expected1
        assert output2 == expected2
        
if __name__ == '__main__':
    unittest.main()


"""
Runtime: 472 ms, faster than 82.21% of Python3 online submissions for Island Perimeter.
Memory Usage: 15.1 MB, less than 17.45% of Python3 online submissions for Island Perimeter.
"""
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 15:00:57 2020

62. Unique Paths (Medium)
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Example 1:

Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
Example 3:

Input: m = 7, n = 3
Output: 28
Example 4:

Input: m = 3, n = 3
Output: 6
 

Constraints:

1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 109.

@author: xingya

"""

## Node, this solution is originally designed by Xingya! Thanks to the previous dynamic practical experience. Great solution!

class Solution:
    def uniquePaths(self, m, n) -> int:
        
        grid = [[1] * n for _ in range(m) ]
        
        for i in range(1, m, 1):
            for j in range(1, n, 1):
                grid[i][j] = grid[i][j-1] + grid[i-1][j]
        
        return grid[-1][-1]
        
        
class Test:
    def testUniquePaths(self)     :
        m = 3
        n = 7
        expected = 28
        
        s = Solution()
        output = s.uniquePaths(m, n)
        
        print(output)
        assert output == expected
        
        
t =Test()
t.testUniquePaths()


"""
Runtime: 16 ms, faster than 99.89% of Python3 online submissions for Unique Paths.
Memory Usage: 14.1 MB, less than 99.96% of Python3 online submissions for Unique Paths.  
""" 
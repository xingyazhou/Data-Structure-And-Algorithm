# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 13:40:34 2020

1351. Count Negative Numbers in a Sorted Matrix (Easy)

Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 

Return the number of negative numbers in grid.
Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
Example 3:

Input: grid = [[1,-1],[-1,-1]]
Output: 3
Example 4:

Input: grid = [[-1]]
Output: 1

@author: xingya
"""


class Solution:
    def countNegatives(self, grid) :    
        if len(grid) == 0:
            return 0
             
        count = [0]
        for i in range(len(grid)):
            self.bs(grid[i], 0, len(grid[0])-1, count) 
           
        return count[0]
    
    def bs(self, gr, l, r, count):
        if l <= r:
            m = (l + r) // 2
           
            if gr[m] < 0 and m == 0:
                count[0] += len(gr) - m
                
            elif gr[m] < 0 and m != 0 : 
                if gr[m-1] >= 0:
                    count[0] = count[0] + len(gr) - m
                    
                else:
                    self.bs(gr, l, m-1, count)
              
                    
            elif gr[m] >= 0: 
                self.bs(gr, m+1, r, count)
                
class Test:
    def testCountNegatives(self):
        
        grid1 = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
        grid2 = [[1,-1],[-1,-1]]
        
        expected1 = 8
        expected2 = 3
        
        s = Solution()
        output1 = s.countNegatives(grid1)
        output2 = s.countNegatives(grid2)

        print(output1)
        print(output2)
        
        assert output1 == expected1, "Wrong output, expected output is: 8"
        assert output2 == expected2, "Wrong output, expected output is :3"
        
t = Test()
t.testCountNegatives()

"""
Runtime: 112 ms, faster than 98.01% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
Memory Usage: 14.8 MB, less than 38.59% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
"""





# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 23:08:54 2020
74. Search a 2D Matrix (Medium)

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
@author: xingya
"""

class Solution:
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0:
            return False

        cn = len(matrix[0])
        return self.bs(matrix, 0, cn * len(matrix)-1, target,  cn )
          
        
    def bs(self, matrix, l, r, target,  cn):
        
        if l<=r:
            
            m = (l+r) // 2
            i = m // cn
            j = m % cn
           
            if matrix[i][j] == target:
                return True
            
            elif matrix[i][j] > target:
                return self.bs(matrix, l, m-1, target,  cn)
                
            elif matrix[i][j] < target:
                return self.bs(matrix, m+1, r, target,  cn)
        
        return False


class Test:
    def testSearchMatrix(self):
  
        matrix = [
          [1,   3,  5,  7],
          [10, 11, 16, 20],
          [23, 30, 34, 50]
        ]
        target1 = 3
        target2 = 13
        
        expected1 = True
        expected2 = False
        
        s =Solution()
        output1 = s.searchMatrix(matrix, target1)
        output2 = s.searchMatrix(matrix, target2)
        
        print(output1)
        print(output2)
        
        assert output1 == expected1, "Wrong result, expected result is: True"
        assert output2 == expected2, "Wrong result, expected result is: False"
        
t = Test()
t.testSearchMatrix()
        

"""
Runtime: 56 ms, faster than 98.72% of Python3 online submissions for Search a 2D Matrix.
Memory Usage: 15.9 MB, less than 56.73% of Python3 online submissions for Search a 2D Matrix.
"""    
            
            
            
            
            
            
 

# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 09:32:01 2020

4Sum II

Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

@author: xingya

"""

from collections import defaultdict

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        d1 = defaultdict(int) 

        n = len(A)
        if n == 0:
            return 0
              
        for i in range(n):
             for j in range(n):
                 d1[A[i] + B[j]] += 1
                 
        count = 0
        for i in range(n):
            for j in range(n):
                
                key = -(C[i] + D[j])
                if  key in d1:
                    count += d1[key]

        return count
                
s = Solution()   
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
print(s.fourSumCount(A,B, C, D))  
         
# Output
# 2

"""
Runtime: 288 ms, faster than 70.30% of Python online submissions for 4Sum II.
Memory Usage: 35.1 MB, less than 90.02% of Python online submissions for 4Sum II.
"""
            
        
        
        
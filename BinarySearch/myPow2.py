# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 20:40:51 2020
50. Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (i.e. xn).

Example 1:

Input: 
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

@author: xingy
"""
import unittest

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """     
        b = bin(n)[2:]
        b = b[::-1]
  
        m = []
        for i in range(len(b)):
            
            if b[i] == '1':
                
                y = x
                for _ in range(i):
                    y *= y
                m.append(y)
                
        mp = 1      
        for d in m:
            mp *= d
            
        return mp
            
class Test(unittest.TestCase):    
        
    def testMyPow(self):
        print("\nStart Testing myPow ...")
        x1 = 2.00000
        n1 = 10     
        expected1 = 1024.0
 
        solution = Solution()
        output1 = solution.myPow(x1, n1)
        
        print("\nMy power is: ", output1)
        assert output1 == expected1
          
 
if __name__ == '__main__':
    unittest.main()           

     
"""
Runtime: 20 ms, faster than 98.53% of Python3 online submissions for Pow(x, n).
Memory Usage: 14.2 MB, less than 99.99% of Python3 online submissions for Pow(x, n).
"""


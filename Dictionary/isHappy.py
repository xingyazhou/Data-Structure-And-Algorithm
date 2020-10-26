# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 21:23:05 2020

202. Happy Number (Easy)

Write an algorithm to determine if a number n is "happy".
A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

@author: xingya
"""

import unittest

class Solution:
    def isHappy(self, n) :
        
        d = set()
        def helper(n): 
            s = str(n)
            m = 0
         
            for c in s:        
                i = int(c)
                m += i*i
                
            if m == 1:
                return True
                
            if m in d:
                return False
 
            d.add(m)
            return helper(m)
                    
        return helper(n)   
                    
class Test(unittest.TestCase):
    def testIsHappy(self):
        print("\n\nStart testing isHappy ...")
        n1 = 19
        expected1 = True
        
        n2 = 18
        expected2 = False
        
        s = Solution()
        output1 = s.isHappy(n1)
        output2 = s.isHappy(n2)
        
        print(n1, output1)
        print(n2, output2)
        assert output1 == expected1
        assert output2 == expected2
    

if __name__ == '__main__':
    unittest.main()
                
"""
Runtime: 24 ms, faster than 98.23% of Python3 online submissions for Happy Number.
Memory Usage: 14.1 MB, less than 99.96% of Python3 online submissions for Happy Number.
'"""
                    
                
                
            
        
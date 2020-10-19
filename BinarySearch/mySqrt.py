# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 22:03:52 2020

69. Sqrt(x) (Easy)

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.

@author: xingy
"""

import unittest

class Solution:
    def mySqrt(self, x: int) -> int:
        
        # user built in function math.sqrt()
        # return int(math.sqrt(x))

        if x <= 1:
            return x

        def bs(x, l, r):          
            if l<= r:
                m = (l+r) // 2
                
                if m * m <= x  and  (m+1) * (m+1) > x:
                    return m
                
                elif m * m > x:
                    return bs(x, l, m-1)
                
                else:
                    return bs(x, m+1, r)
                
        return bs(x, 0, x-1)
    
    

class Test(unittest.TestCase):
    def testMySqrt(self):
        print("\nStart testing mySqrt ...")
        
        x = 8
        expected_output = 2
        
        s = Solution()
        output = s.mySqrt(x)
        
        print("mySqrt(", x, ") is : ", output)
        assert output == expected_output


if __name__ == '__main__':
    unittest.main()
                

"""
Runtime: 32 ms, faster than 82.78% of Python3 online submissions for Sqrt(x).
Memory Usage: 14.1 MB, less than 99.96% of Python3 online submissions for Sqrt(x).
"""
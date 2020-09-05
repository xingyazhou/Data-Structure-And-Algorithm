# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 17:50:56 2020


50. Pow(x, n)
Medium
Implement pow(x, n), which calculates x raised to the power n (i.e. xn).

 
Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104

@author: xingya
"""


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """  
        
        b=bin(n)[2:]
        
        s=x
        myPower=1
        r=[]
        
        for i,q in enumerate(b):
            p = len(b) - i -1
            
            if q=='1':
                for i in range(p):
                    s = s*s
                r.append(s)
                s=x
                
        for x in r:
             myPower = x*myPower
                         
        return(myPower)
            

s = Solution()
print(s.myPow(3, 5))

# Output
# 243

"""
Runtime: 16 ms, faster than 90.81% of Python online submissions for Pow(x, n).
Memory Usage: 12.6 MB, less than 95.73% of Python online submissions for Pow(x, n).
"""
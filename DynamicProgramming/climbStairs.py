# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 11:24:36 2020

70. Climbing Stairs (Easy)
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:

1 <= n <= 45

@author: xingya

"""

class Solution(object):
    """
    One can reach  i step in one of the two ways:
    1. Taking a single step from (i-1) step.
    2. Taking a step of 2 from (i-2) step.
    """
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = [0] * (n+1)
      
        f[1] = 1
        f[2] = 2
        
        for i in range(3,n+1):
            f[i] = f[i-1] + f[i-2]
         

        return f[n]
    
n = 3
s = Solution()
print(s.climbStairs(n))

# Output
# 3



"""      
Runtime: 12 ms, faster than 95.34% of Python online submissions for Climbing Stairs.
Memory Usage: 13.4 MB, less than 5.25% of Python online submissions for Climbing Stairs.
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 20:06:53 2020

367. Valid Perfect Square

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

Example 1:

Input: num = 16
Output: true
Example 2:

Input: num = 14
Output: false
 
Constraints:
1 <= num <= 2^31 - 1

@author: xingya

"""

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        
        return self.binarysearch(num, 0, num-1)
            
    def binarysearch(self, num, l, r):
        if l <= r:
            
            mi = (l+r) // 2
            
            if mi * mi == num:
                return True
            
            if mi * mi > num:
                return self.binarysearch(num, l, mi-1)
            
            if mi * mi < num:
                return self.binarysearch(num, mi+1, r)
    
        return False
    
        
s = Solution()
print(s.isPerfectSquare(625))
print(s.isPerfectSquare(14))
print(s.isPerfectSquare(1))

# Output
# True
                
"""
Runtime: 12 ms, faster than 97.73% of Python online submissions for Valid Perfect Square.
Memory Usage: 12.6 MB, less than 83.74% of Python online submissions for Valid Perfect Square.
"""
            
            
        
        

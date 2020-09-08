# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 20:43:06 2020

287. Find the Duplicate Number

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one duplicate number in nums, return this duplicate number.

Follow-ups:

How can we prove that at least one duplicate number must exist in nums? 
Can you solve the problem without modifying the array nums?
Can you solve the problem using only constant, O(1) extra space?
Can you solve the problem with runtime complexity less than O(n2)?
 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [1,1]
Output: 1
Example 4:

Input: nums = [1,1,2]
Output: 1

@author: xingy
"""



from collections import defaultdict
class Solution:
    def findDuplicate(self, nums) :
        d={}
        for x in nums:
            if x in d:
                return x
            else:
                d[x] = 1
            
        
          
nums = [1,3,4,2,2]
s=Solution()
print(s.findDuplicate(nums))


# Output
# 2

"""
Runtime: 60 ms, faster than 96.35% of Python3 online submissions for Find the Duplicate Number.
Memory Usage: 16.2 MB, less than 83.87% of Python3 online submissions for Find the Duplicate Number.
"""
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 17:10:11 2020

Leetcode

136. Single Number
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4

@author: xingya
"""

def singleNumber(nums):
    """
    Approach : Hash Table (Dictionary)
    Algorithm
    Use hash table to avoid the O(n) time required for searching the elements.
    """
    
    d = {}
    for x in nums:
        if x not in d:
            d[x] = 1
        else:
            d.pop(x)
   
    return list(d.keys())[0]
    
nums = [4,1,2,1,2]
print(singleNumber(nums))

# Output
# 4


"""
Runtime: 60 ms, faster than 99.45% of Python online submissions for Single Number.
Memory Usage: 15.2 MB, less than 23.14% of Python online submissions for Single Number.
"""
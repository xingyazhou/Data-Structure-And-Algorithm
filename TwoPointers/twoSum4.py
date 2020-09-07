# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 13:21:07 2020

Two Sum II - Input array is sorted

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
 

Constraints:

2 <= nums.length <= 3 * 104
-1000 <= nums[i] <= 1000
nums is sorted in increasing order.
-1000 <= target <= 1000


@author: xingya

"""



class Solution:
    def twoSum(self, numbers, target):
        
        l=0
        r = len(numbers) - 1
        
        while l < r:
            
            if numbers[l] + numbers[r] == target:
                return ([l+1, r+1])
            
            elif numbers[l] + numbers[r] > target:
                r -= 1
                
            elif numbers[l] + numbers[r] < target:
                l += 1
            
        return ([-1,-1])
        
s= Solution()      
print(s.twoSum([1,2,3,4,5,6,89], 11))

# Output
# [5,6]
        
        
        
"""       
Runtime: 64 ms, faster than 80.63% of Python3 online submissions for Two Sum II - Input array is sorted.
Memory Usage: 14.3 MB, less than 57.58% of Python3 online submissions for Two Sum II - Input array is sorted.
"""



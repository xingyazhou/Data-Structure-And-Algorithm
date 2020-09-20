# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 16:31:29 2020

1. Two Sum (Easy)
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

2 <= nums.length <= 105
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.


@author: xingya

"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        d  = defaultdict(list)       
        
        for i in range(len(nums)):
            d[nums[i]].append(i)
            
        for i in range(len(nums)):
            y = target - nums[i]
            
            if y in d:
                
                if nums[i]!=y:
                    return [i, d[y][0]]
                
                else:
                    if len(d[y]) >=2 :
                        
                        return [i, d[y][1]]
                    
s = Solution()
print(s.twoSum([2,7,11,15], 9))

# Output
# [0, 1]
                    
"""                   
Runtime: 36 ms, faster than 86.34% of Python online submissions for Two Sum.
Memory Usage: 15.5 MB, less than 5.00% of Python online submissions for Two Sum.    
     
"""          
        
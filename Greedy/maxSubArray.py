# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 22:25:24 2020

53. Maximum Subarray (Easy)
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [0]
Output: 0
Example 4:

Input: nums = [-1]
Output: -1
Example 5:

Input: nums = [-2147483647]
Output: -2147483647
 

Constraints:

1 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1

Greedy: Pick the locally optimal move at each step, and that will lead to the globally optimal solution.

@author: xingya

"""

import sys

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        maxSumAtCurrentPosition = 0
        maxSubArraySum = -sys.maxsize - 1
        
        for i in range(len(nums)):
                 
            maxSumAtCurrentPosition = max(maxSumAtCurrentPosition + nums[i], nums[i] )               
            maxSubArraySum = max(maxSubArraySum, maxSumAtCurrentPosition)
                   
        return maxSubArraySum
    
    

nums = [-2,1,-3,4,-1,2,1,-5,4]
s = Solution()    
print(s.maxSubArray(nums))

# Output
# 6

# Time complexity : O(N) since it's one pass along the array.
# Space complexity : O(1), since it's a constant space solution.

"""
Runtime: 44 ms, faster than 97.16% of Python online submissions for Maximum Subarray.
Memory Usage: 13.2 MB, less than 64.37% of Python online submissions for Maximum Subarray.
"""




            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        


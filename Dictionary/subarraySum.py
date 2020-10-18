# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 22:58:48 2020

560. Subarray Sum Equals K (Medium)

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2

Constraints:

The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

@author: xingya
"""

import unittest
from collections import defaultdict
class Solution:
    def subarraySum(self, nums, k) :
        
        count = 0
        s = 0      
        d = defaultdict(int)
        
        for i in range(0,len(nums)):
            
            s += nums[i]
            if s - k in d:
                count += d[s-k]
            
            if s == k:
                count += 1
                
            d[s] += 1
            
        return count
    
class Test(unittest.TestCase):
    def testsubarraySum(self):
        
        nums1 = [3,4,7,2,-3,1,4,2]
        k1 = 7
        expected1 = 4
        
        s = Solution()
        output1 = s.subarraySum(nums, k1)
        
        print("\nTest Case 1: nums = ", nums1, ", k = ", k1)
        print("The total number of continuous subarrays: ", output1)
        assert output1 == expected1
        
        nums2 = [1,1,1]
        k2=2
        expected2 = 2
        output2 = s.subarraySum(nums2, k2)
        print("\nTest Case 2: nums = ", nums2, ", k = ", k2)
        print("The total number of continuous subarrays: ", output2)
        assert output2 == expected2
       
        
if __name__ == '__main__':
    unittest.main()
        

  
"""          
Runtime: 128 ms, faster than 91.31% of Python3 online submissions for Subarray Sum Equals K.
Memory Usage: 16.3 MB, less than 18.53% of Python3 online submissions for Subarray Sum Equals K.
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 21:06:15 2020

1512. Number of Good Pairs (Easy)

Given an array of integers nums.
A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0

@author: xingya
"""

from collections import defaultdict
import unittest

class Solution:
    def numIdenticalPairs(self, nums):
        
        output = 0
        
        d = defaultdict(int)        
        for x in nums:
            d[x] += 1
            
        for v in d.values():
            output += (v-1)*v // 2
        
        return output


class Test(unittest.TestCase):
    def testNumIdenticalPairs(self):
        print("\n\nTesting numIdenticalpairs ...")
        
        nums1 = [1,2,3,1,1,3]
        expected1 = 4
        
        nums2 = [1,1,1,1]
        expected2 = 6
        
        s = Solution()
        output1 = s.numIdenticalPairs(nums1)
        output2 = s.numIdenticalPairs(nums2)
        
        print(output1, output2)
        assert output1 == expected1
        assert output2 == expected2

if __name__ == "__main__":
    unittest.main()
    
    
    
"""
Runtime: 24 ms, faster than 97.14% of Python3 online submissions for Number of Good Pairs.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Number of Good Pairs.
"""
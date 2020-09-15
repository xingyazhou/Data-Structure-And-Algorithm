# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 22:01:31 2020

Intersection of Two Arrays
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.

@author: xingya
"""

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        d = {}
        l=[]
        
        for x in nums1:
            if x not in d:
                d[x] = 1
                
        for x in nums2:
          
            if x in d:
                l.append(x)
                d.pop(x)
                
        return l
    
s=Solution()
print(s.intersection([4,9,5],[9,4,9,8,4]))

"""   
Runtime: 28 ms, faster than 94.25% of Python online submissions for Intersection of Two Arrays.
Memory Usage: 12.8 MB, less than 64.65% of Python online submissions for Intersection of Two Arrays.
"""
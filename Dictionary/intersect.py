# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 15:39:09 2020

350. Intersection of Two Arrays II
(Easy)

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?


@author: xingya

"""

from collections import defaultdict

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l=[]
        d1 = defaultdict(int)
        
        if len(nums1) >= len(nums2):
           
            for x in nums1:
                d1[x] += 1

            for y in nums2:
                if y in d1 and d1[y]>0:
                    l.append(y)
                    d1[y]-=1
                           
        else:
            for x in nums2:
                d1[x] += 1
    
            for y in nums1:
                if y in d1 and d1[y] > 0:
                    l.append(y)
                    d1[y]-=1
                          
        return l
    
nums1 = [4,9,5,4,4]  
nums2 = [9,4,9,8,4] 
s = Solution()
print(s.intersect(nums1,nums2))

# Output
# [9,4,4]

# Time Complexity: \mathcal{O}(n + m)O(n+m), where nn and mm are the lengths of the arrays
    
    
    
"""    
Runtime: 36 ms, faster than 76.38% of Python online submissions for Intersection of Two Arrays II.
Memory Usage: 12.9 MB, less than 49.69% of Python online submissions for Intersection of Two Arrays II.
"""
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 11:49:34 2020

4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Follow up: The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000
Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000

@author: xingya
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        s = nums1 + nums2
        n=len(s) 
        i = n// 2
        
        if n == 1:
            return s[0]
        
        if len(nums1) != 0 and len(nums2) !=0:
            self.bs_mergesort(s)
        
        #print(n,s)
        
        if n % 2 == 1:
            m = s[i]
        else:
            m = (s[i] + s[i-1]) / 2
        return m
        
    def bs_mergesort(self, a):
        
        n = len(a)
        if n>1:
            mi = n // 2
            l = a[:mi]
            r = a[mi:]
            
            self.bs_mergesort(l)
            self.bs_mergesort(r)
            
            i = 0
            j = 0
            k = 0
            
            while i < len(l) and j < len(r):
                if l[i] <= r[j]:
                    a[k] = l[i]
                    i+=1
                    k+=1
                else:
                    a[k]= r[j]
                    j+=1
                    k+=1
            
            while i <len(l):
                a[k] = l[i]
                i+=1
                k+=1
                
            while j < len(r):
                a[k] = r[j]
                j+=1
                k+=1
                
        return a
    
          
nums1=[1,2]
nums2=[3,4]
s=Solution()
print(s.findMedianSortedArrays(nums1,nums2))

# Output 


"""
Performance is NOT good, need to be improved

Runtime: 188 ms, faster than 6.87% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 14 MB, less than 51.87% of Python3 online submissions for Median of Two Sorted Arrays.
"""
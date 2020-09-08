# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 21:27:15 2020

153. Find Minimum in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0

@author: xingya


"""



class Solution:
    def findMin(self,a):
        return self.bs(nums, 0, len(nums)-1)

    
    def bs(self, a, l, r):
        if r-l == 1:
            return min(a[l], a[r])
   
        if r == l:
            return a[l]
        
        if l<r:
            m = (l+r)//2
      
            if a[l] < a[m] and a[m]> a[r]:
                return self.bs(a, m+1,r)
            
            elif a[l] > a[m] and a[m] < a[r]:
                
                if a[m] <a[m-1] and a[m] <a[m+1]:
                    return a[m]
                
                else:
                    return self.bs(a, l, m-1)
                           
            else:
                return a[l]
            
        
nums = [4,5,6,7,0,1,2]
s = Solution()
print(s.findMin(nums))

            
"""          
Runtime: 36 ms, faster than 93.20% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
Memory Usage: 14.2 MB, less than 8.76% of Python3 online submissions for Find Minimum in Rotated Sorted Array.   
"""

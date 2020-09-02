# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 19:31:40 2020

@author: xingy
"""
import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.org = list(nums)
        self.nums = nums


    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.nums = list(self.org)
        #self.org= list(self.org)
        return self.nums
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in range(len(self.nums)):
            r = random.randrange(i, len(self.nums))
            self.nums[i], self.nums[r] = self.nums[r], self.nums[i]
        
        return self.nums
    
s = Solution([1,2,3])

print( s.shuffle())
print(s.reset())
print("\n")

print(s.shuffle())
print(s.reset())
print("\n")

print( s.shuffle())
print(s.reset())
print("\n")
print(s.shuffle())
print(s.reset())




# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 14:46:14 2020
303. Range Sum Query - Immutable (Easy)

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int i, int j) Return the sum of the elements of the nums array in the range [i, j] inclusive (i.e., sum(nums[i], nums[i + 1], ... , nums[j]))
 
Example 1:

Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1)) 
numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))

@author: xingy
"""

class NumArray:

    def __init__(self, nums):
        self.arr = nums
        self.sum = [0] * len(self.arr)
        
        if len(nums) > 0:
            self.sum[0] = nums[0]      
            for i in range(1, len(self.arr), 1):
                self.sum[i] = self.sum[i-1] +self.arr[i]

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.sum[j]
        else:
            
            return self.sum[j] -self.sum[i-1]
        
class Test:
    def testSumRange(self):
        nums = [-2, 0, 3, -5, 2, -1]
        s = NumArray(nums)
        
        expect1 = 1
        expect2 = -1
        expect3 = -3
             
        output1 = s.sumRange(0,2)
        output2 = s.sumRange(2,5)
        output3 = s.sumRange(0,5)
        
        print(output1, output2, output3)
        
        assert output1 == expect1
        assert output2 == expect2
        assert output3 == expect3
        

t = Test()
t.testSumRange()

"""
Runtime: 64 ms, faster than 99.87% of Python3 online submissions for Range Sum Query - Immutable.
Memory Usage: 17.6 MB, less than 37.73% of Python3 online submissions for Range Sum Query - Immutable.
"""
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 23:05:28 2020

170. Two Sum III - Data structure design

Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Example 1:

add(1); add(3); add(5);
find(4) -> true
find(7) -> false
Example 2:

add(3); add(1); add(2);
find(3) -> true
find(6) -> false

@author: xingya

"""

from collections import defaultdict
class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = defaultdict(int)

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
       
        self.d[number] += 1
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for x in self.d.keys():
            
            y = value - x
            if y in self.d and y!=x:
                return True
                break
            
            if y==x and self.d[x]>=2:
                return True
            
        return False
    

twoSum = TwoSum()

twoSum.add(0)
twoSum.add(0)
twoSum.add(0)
print(twoSum.find(0))
print(twoSum.find(6))

# Output
# True
# False


"""
Runtime: 324 ms, faster than 85.87% of Python online submissions for Two Sum III - Data structure design.
Memory Usage: 19.4 MB, less than 50.00% of Python online submissions for Two Sum III - Data structure design.
"""


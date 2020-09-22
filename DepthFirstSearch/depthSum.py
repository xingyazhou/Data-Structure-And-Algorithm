# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 19:17:43 2020

339. Nested List Weight Sum

Share
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: 10 
Explanation: Four 1's at depth 2, one 2 at depth 1.
Example 2:

Input: [1,[4,[6]]]
Output: 27 
Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27.

@author: xingya

"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

"""
This Solution is not originally created by Xingya. 
Key point: weight is append to stack together with the nestedList.
"""

class Solution:
    def depthSum(self, nestedList):  
        
        stack = [[1, nestedList]]
        count = 0
        while len(stack):
            weight, nest = stack.pop()
            for i in nest:
                if i.isInteger():
                    count += i.getInteger() * weight
                else:
                    stack.append([weight + 1, i.getList()])
            
        return count
                    

"""
Runtime: 28 ms, faster than 87.68% of Python3 online submissions for Nested List Weight Sum.
Memory Usage: 13.9 MB, less than 91.86% of Python3 online submissions for Nested List Weight Sum.
"""


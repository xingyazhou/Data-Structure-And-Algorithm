# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 20:24:41 2020

437. Path Sum III (Medium)

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

Return 3. The paths that sum to 8 are:
    
      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11

@author: xingya

Note: This algorithm is not originally created by Xingya
https://leetcode.com/problems/path-sum-iii/solution/

"""

# preorder: left, right, node

from collections import defaultdict
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    
    def pathSum(self, root, sum) :
        
        def preorder(node, curr_sum):

            if node is None:
                return 
            
            nonlocal count
            curr_sum += node.val

            if curr_sum == k:
                count += 1
            
            if curr_sum - k in h:
                count += h[curr_sum - k]

            h[curr_sum] += 1
            
            preorder(node.left, curr_sum)
            preorder(node.right, curr_sum)
            
            # remove curr_sum in the hashmap
            h[curr_sum] -= 1
            
        count, k = 0, sum    
        h = defaultdict(int)
        
        preorder(root, 0)
        
        return count
            
class Test:
    def testPathSum(self):
        
        # Build a tree
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(-3)
        
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(2)
        root.right.right = TreeNode(11)
        
        root.left.left.left = TreeNode(3)
        root.left.left.right = TreeNode(-2)
        root.left.right.right = TreeNode(1)
        
        expect = 3
    
        s = Solution()
        output = s.pathSum(root, 8)
        
        print(" The paths that sum to 8 are: ", output)
        assert output == expect
        
t = Test()
t.testPathSum()

"""
Runtime: 48 ms, faster than 88.27% of Python3 online submissions for Path Sum III.
Memory Usage: 15.4 MB, less than 8.89% of Python3 online submissions for Path Sum III.
"""

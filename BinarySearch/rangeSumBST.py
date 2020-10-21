# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 21:15:46 2020

938. Range Sum of BST (Easy)

Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23

Note:

The number of nodes in the tree is at most 10000.
The final answer is guaranteed to be less than 2^31.

@author: xingya
"""

import unittest

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
                                  
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int: 
        def helper(root, L, R):
            
            nonlocal s
            if root is not None:
            
                if root.val < L:
                    helper(root.right, L, R)

                if root.val > R:
                    helper(root.left, L, R)

                if root.val >= L and root.val <=R:
                    s += root.val
                    helper(root.left, L, R)
                    helper(root.right, L, R)
             
        s = 0
        helper(root, L, R)
        
        return s

class Test(unittest.TestCase):
    def testRangeSumBST(self):
        
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)
        root.right.right = TreeNode(18)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(7)
        L = 7
        R = 15
        
        expected = 32
        
        s = Solution()
        output = s.rangeSumBST(root, L, R)
        
        print("\nThe sum of values: ", output)
        assert output == expected
    
if __name__ == '__main__':
    unittest.main()

"""
Runtime: 196 ms, faster than 98.62% of Python3 online submissions for Range Sum of BST.
Memory Usage: 22.1 MB, less than 99.95% of Python3 online submissions for Range Sum of BST.
"""
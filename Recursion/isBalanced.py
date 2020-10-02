# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 11:49:34 2020

110. Balanced Binary Tree (Easy)
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:
Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.

@author: xingya
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """  
        isbanced, h = self.getDepth(root)       
        return isbanced
        
    def getDepth(self, root):
        if root is None:
            return True, 0
        
        else:
            isbalanced_l, d_l = self.getDepth(root.left)
            isbalanced_r, d_r = self.getDepth(root.right)
            
            isbalanced_tree = isbalanced_l and isbalanced_r and abs(d_l - d_r) <= 1
            h = max(d_l, d_r) + 1
            return isbalanced_tree, h
        
class Test():
    def testIsBalancedTree(self):
        
        root1 = TreeNode(1)
        root1.left = TreeNode(2)
        root1.right = TreeNode(2)
        root1.left.left = TreeNode(3)
        root1.left.left.right = TreeNode(4)
        root1.left.left.right.left = TreeNode(4)
        root1.left.left.left = TreeNode(3)
        
        root2 = TreeNode(3)
        root2.left = TreeNode(9)
        root2.right = TreeNode(20)
        root2.right.left = TreeNode(15)
        root2.right.right = TreeNode(7)
        
        expected_output1 = False
        expected_output2 = True
        
        s = Solution()
        output1 = s.isBalanced(root1)
        output2 = s.isBalanced(root2)
        
        print(output1)
        print(output2)
        
        assert (output1 == expected_output1), "Wrong result, expected output is :False"
        assert (output2 == expected_output2), "Wrong result, expected output is :True"
        

t=Test()
t.testIsBalancedTree()

"""
Runtime: 32 ms, faster than 97.93% of Python online submissions for Balanced Binary Tree.
Memory Usage: 18 MB, less than 42.27% of Python online submissions for Balanced Binary Tree.
"""
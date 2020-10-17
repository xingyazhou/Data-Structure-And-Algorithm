# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 20:14:31 2020

543. Diameter of Binary Tree (Easy)

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.

@author: xingy
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        count = [0]
        self.getDepthOfTree(root, count)

        return count[0]
        
        
    def getDepthOfTree(self, root, count):
        if root is None:
            return 0
        
        leftDepth = self.getDepthOfTree(root.left, count)
        rightDepth = self.getDepthOfTree(root.right, count)
        
        count[0] = max(count[0], leftDepth + rightDepth)
        return 1 + max(leftDepth, rightDepth)
    
class Test:
    def testDiameterOfBinayTree(self):
        # Buid a Tree
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        
        expected_pathlen = 3

        s = Solution()
        # Calculate the longest length of the path
        pathlen = s.diameterOfBinaryTree(root)
        
        print(pathlen)
        assert pathlen == expected_pathlen
        
t = Test()
t.testDiameterOfBinayTree()

        
"""
Runtime: 32 ms, faster than 99.49% of Python3 online submissions for Diameter of Binary Tree.
Memory Usage: 15.7 MB, less than 88.04% of Python3 online submissions for Diameter of Binary Tree.
"""
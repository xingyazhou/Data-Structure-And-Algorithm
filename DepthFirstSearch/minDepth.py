# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 16:00:27 2020

111. Minimum Depth of Binary Tree (Easy)
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.

@author: xingya

"""

import sys
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
                  
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root is None:
            return 0
        
        minD = sys.maxsize
        stack = [(root, 1)]
        
        while stack:
            
            node, depth = stack.pop()
            
            if node.left is None and node.right is None:
                minD = min(minD, depth)
                
            if node.left:
                stack.append((node.left, depth+1))
                
            if node.right:
                stack.append((node.right, depth+1))
    
        return minD
        
                
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)  
root.right.left = TreeNode(15)      
root.right.right = TreeNode(7)

s = Solution()
print(s.minDepth(root))

# Output
# 2

"""
Runtime: 32 ms, faster than 85.01% of Python online submissions for Minimum Depth of Binary Tree.
Memory Usage: 15.5 MB, less than 78.79% of Python online submissions for Minimum Depth of Binary Tree.
"""




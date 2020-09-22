# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 14:02:27 2020

104. Maximum Depth of Binary Tree (Easy)

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

@author: xingya

"""


# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """                       
        if root is None:
            return 0
             
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

s = Solution()
print(s.maxDepth(root))

# Output
# 3


"""
Runtime: 32 ms, faster than 69.65% of Python online submissions for Maximum Depth of Binary Tree.
Memory Usage: 15.4 MB, less than 81.23% of Python online submissions for Maximum Depth of Binary Tree.
"""
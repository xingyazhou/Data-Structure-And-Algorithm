# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 21:03:24 2020

108. Convert Sorted Array to Binary Search Tree (Easy)

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

@author: xingya

"""
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def sortedArrayToBST(self, a):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """ 
        if not a:
            return None
        
        m = len(a) // 2 
        root = TreeNode(a[m])
        
        root.left = self.sortedArrayToBST(a[:m])
        root.right = self.sortedArrayToBST(a[m+1:])
        
        return root
    
    def inorder(self, root, output):
        if root:
            self.inorder(root.left, output)
            output.append(root.val)
            self.inorder(root.right, output)
            
        return output
    
nums = [-10,-3,0,5,9]
s = Solution()
root = s.sortedArrayToBST(nums)
print(s.inorder(root, output=[]))

# Output 
# [-10, -3, 0, 5, 9]

"""
Runtime: 72 ms, faster than 85.81% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
Memory Usage: 16 MB, less than 90.22% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 20:57:41 2020

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

@author: xingya
"""

from collections import defaultdict
import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def zigzagLevelOrder(self, root):
        
        if root is None:
            return []
        
        q = [(0, root)]
        output = defaultdict(list)
        
        while q:
            level, node = q.pop()
           
            if node.left:
                q.insert(0, (level+1, node.left))
            if node.right:
                q.insert(0, (level+1, node.right))
                
            if level % 2 == 0:
                output[level].append(node.val)
            else:
                output[level].insert(0, node.val)               
                          
        return list(output.values())
        
class Test(unittest.TestCase):
    def testZigzagLevelOrder(self):
        print("\n\nTesting zigzaglevelOrder ...")
        # build a Tree
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        
        expected = [[3], [20,9], [15,7]]
        
        s = Solution()
        output = s.zigzagLevelOrder(root)
        
        print(output)
        assert output == expected
        
if __name__ == "__main__":
    unittest.main()
                   
"""        
Runtime: 24 ms, faster than 97.15% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Binary Tree Zigzag Level Order       
"""
        
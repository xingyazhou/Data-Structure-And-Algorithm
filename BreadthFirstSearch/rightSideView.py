# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 14:36:29 2020
199. Binary Tree Right Side View (Medium)

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

@author: xingya

"""


# Definition for a binary tree node.
from collections import defaultdict

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.bfs(root)
        
    def bfs(self, root):
        
        if root is None:
            return
       
        depth = 1
        queue = [(root, depth)]
        d = defaultdict(list)
        output = []

        while queue:
            node, depth = queue.pop(0)
            d[depth].append(node.val)
            
            if node.left:
                queue.append((node.left, depth+1))
                
            if node.right:
                queue.append((node.right,depth+1))
                
        for key in d:
            output.append(d[key][-1])
                
        return output
  
    

def assert_check():
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    # Construct following tree
    """
       1            <---
     /   \
    2     3         <---
     \     \
      5     4       <---
    """
    
    s = Solution()
    result = s.rightSideView(root)
    
    assert (result == [1, 3, 5]), "Wrong output, Expected result [1, 3, 5]"
    print(result)
    
assert_check()
    
# Output
# [1,3,5]

"""
Runtime: 8 ms, faster than 99.77% of Python online submissions for Binary Tree Right Side View.
Memory Usage: 12.7 MB, less than 54.71% of Python online submissions for Binary Tree Right Side View.
"""

        
        


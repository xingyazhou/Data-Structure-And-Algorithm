# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 21:55:29 2020

559. Maximum Depth of N-ary Tree (Easy)

Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).


Example 1:

Input: root = [1,null,3,2,4,null,5,6]
Output: 3
Example 2:


@author: xingy
"""


# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        
        if root is None:
            return 0
        
        if root.children is None :
            return 1
          
        height = []
        
        for child in root.children:
            height.append( self.maxDepth(child) )
            
        return max(height) + 1
    
    
root = Node(1)
root.children = [None, Node(3), Node(2), Node(4)]
root.children[1].children = [None, Node(5), Node(6)]

s = Solution()
print(s.maxDepth(root))

# Output
# 3
            
"""
Runtime: 32 ms, faster than 92.49% of Python online submissions for Maximum Depth of N-ary Tree.
Memory Usage: 15.7 MB, less than 98.20% of Python online submissions for Maximum Depth of N-ary Tree.
"""
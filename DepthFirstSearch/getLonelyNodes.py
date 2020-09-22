# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 21:02:34 2020

1469. Find All The Lonely Nodes (Easy)
In a binary tree, a lonely node is a node that is the only child of its parent node. The root of the tree is not lonely because it does not have a parent node.
Given the root of a binary tree, return an array containing the values of all lonely nodes in the tree. Return the list in any order.

Example 1:

Input: root = [1,2,3,null,4]
Output: [4]
Explanation: Light blue node is the only lonely node.
Node 1 is the root and is not lonely.
Nodes 2 and 3 have the same parent and are not lonely.
Example 2:

Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2]
Output: [6,2]
Explanation: Light blue nodes are lonely nodes.
Please remember that order doesn't matter, [2,6] is also an acceptable answer.
Example 3:

Input: root = [11,99,88,77,null,null,66,55,null,null,44,33,null,null,22]
Output: [77,55,33,66,44,22]
Explanation: Nodes 99 and 88 share the same parent. Node 11 is the root.
All other nodes are lonely.
Example 4:

Input: root = [197]
Output: []
Example 5:

Input: root = [31,null,78,null,28]
Output: [78,28]
 
@author: xingya

"""

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def getLonelyNodes(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if root is None:
            return []
        
        if root.left is None and root.right is None:
            return []
           
        lonelyN = []        
        stack = [root]
        
        while stack:
            
            node = stack.pop()
           
            if node.left is None and node.right  :
                stack.append(node.right)
                lonelyN.append(node.right.val)
                
            if  node.left and node.right is None:
                stack.append(node.left)
                lonelyN.append(node.left.val)
                
            if node.left and node.right:
                stack.append(node.left)
                stack.append(node.right)
            
        return lonelyN
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)

s = Solution()
print(s.getLonelyNodes(root))

# Output
# [4]

"""
Runtime: 36 ms, faster than 99.51% of Python online submissions for Find All The Lonely Nodes.
Memory Usage: 13.3 MB, less than 96.57% of Python online submissions for Find All The Lonely Nodes.
"""
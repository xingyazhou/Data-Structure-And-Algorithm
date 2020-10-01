# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 21:57:16 2020

987. Vertical Order Traversal of a Binary Tree (Medium)

Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).

Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, we report the values of the nodes in order from top to bottom (decreasing Y coordinates).

If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.

Example 1:


Input: [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation: 
Without loss of generality, we can assume the root node is at position (0, 0):
Then, the node with value 9 occurs at position (-1, -1);
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
The node with value 20 occurs at position (1, -1);
The node with value 7 occurs at position (2, -2).
Example 2:

Input: [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation: 
The node with value 5 and the node with value 6 have the same position according to the given scheme.
However, in the report "[1,5,6]", the node value of 5 comes first since 5 is smaller than 6.
 
Note:

The tree will have between 1 and 1000 nodes.
Each node's value will be between 0 and 1000.

@author: xingya

"""
## Need to correct the order of output element

from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def verticalTraversal(self, root) : 
        if root is None:
            return []
        
        l = defaultdict(list)
        
        root.x = 0
        root.y = 0
        self.setPostion(root) 
        self.inorder(root, l)
        
        for k in l:
            l[k].sort()
        
        return list(l.values())
        
    def setPostion(self, root):
        if root:
            if root.left:
                root.left.x = root.x - 1
                root.left.y = root.y - 1
            if root.right:
                root.right.x = root.x + 1
                root.right.y = root.y - 1
            self.setPostion(root.left)
            self.setPostion(root.right)
            
    def inorder(self, root, l):
        if root:
            self.inorder(root.left,l)          
            l[root.x].append(root.val)       
            self.inorder(root.right,l)
        
   
        
root = TreeNode(3)       
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
s=Solution()
print(s.verticalTraversal(root))
        
        
        
# Output
# [[9], [3, 15], [20], [7]]        
        
        
        
        
        
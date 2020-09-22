# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 22:47:39 2020

101. Symmetric Tree (Easy)

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Follow up: Solve it both recursively and iteratively.

Note: isMirror(self, t1, t2) function is not originally designed by Xingya

@author: xingya
"""


class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        

class Solution:
    def isSymmetric(self, root) :
        
        if root is None or (root.left is None  and root.right is None):
            return True
          
        if  not root.left or not root.right:
            return False
        
        return self.isMirror(root.left, root.right)
    
    
    def isMirror(self, t1, t2):
    
        if not t1 and not t2: return True
        if not t1 or not t2: return False
        
        return t1.val == t2.val and self.isMirror(t1.right, t2.left) and self.isMirror(t1.left, t2.right)
            

        
root = Node(1)
root.left = Node(2)
root.left.right = Node(2)
root.right = Node(2)
root.right.right = Node(2)

"""
    1
   / \
  2   2
   \   \
   2    2
"""

s = Solution()
print(s.isSymmetric(root))

# Output
# False

"""
Runtime: 12 ms, faster than 99.39% of Python online submissions for Symmetric Tree.
Memory Usage: 12.9 MB, less than 67.03% of Python online submissions for Symmetric Tree.
"""

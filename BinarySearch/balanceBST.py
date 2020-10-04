# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 19:53:28 2020

1382. Balance a Binary Search Tree
Given a binary search tree, return a balanced binary search tree with the same node values.

A binary search tree is balanced if and only if the depth of the two subtrees of every node never differ by more than 1.

If there is more than one answer, return any of them.

Example 1:

Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2,null,null] is also correct.
 
Constraints:

The number of nodes in the tree is between 1 and 10^4.
The tree nodes will have distinct values between 1 and 10^5.

@author: xingya
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right        
        
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        self.inorder(root, arr)
        
        l, r = 0, len(arr) - 1
        m = (l+r) // 2
        balancedT = arr[m]
        balancedT.left = None
        balancedT.right = None
             
        self.bs(arr, l, m-1, balancedT )
        self.bs(arr, m+1, r, balancedT)        
       
        return balancedT
        
    def insert(self, balancedT, node):
        if balancedT:
            
            if node.val <= balancedT.val:
                if balancedT.left is None:
                    balancedT.left = node
                else:
                    self.insert(balancedT.left, node)
            if node.val > balancedT.val:
        
                if balancedT.right is None:
                    balancedT.right = node
                else:
                    self.insert(balancedT.right, node)
                  
    def bs(self, arr, l, r, balancedT):
        if  l <= r:
            m = (l + r) // 2
            arr[m].left = None
            arr[m].right = None
            self.insert(balancedT, arr[m])
            self.bs(arr, l, m-1, balancedT)      
            self.bs(arr, m+1, r, balancedT)           
                              
    def inorder(self, root, arr) :
        if root:
            self.inorder(root.left, arr)
            arr.append(root)
            self.inorder(root.right, arr)


class Test():
    def testBalanceBST(self):

        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        root.right.right.right = TreeNode(4)
        root.right.right.right.right = TreeNode(5)
        
        s = Solution()
        bst = s.balanceBST(root)
        
        
        assert bst.val == 3
        assert bst.left.val == 1
        assert bst.left.right.val == 2
        assert bst.right.val == 4
        assert bst.right.right.val == 5
        
        print("BFS:",[ bst.val, bst.left.val, bst.right.val, bst.left.left, bst.left.right.val, bst.right.left, bst.right.right.val ])
   
t = Test()
t.testBalanceBST()

# Output
# BFS: [3, 1, 4, None, 2, None, 5]

"""
Runtime: 540 ms, faster than 14.10% of Python3 online submissions for Balance a Binary Search Tree.
Memory Usage: 18.4 MB, less than 85.43% of Python3 online submissions for Balance a Binary Search Tree.
"""



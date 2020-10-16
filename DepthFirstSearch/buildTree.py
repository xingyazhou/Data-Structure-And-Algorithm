# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 22:55:11 2020

105. Construct Binary Tree from Preorder and Inorder Traversal (Medium)

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

@author: xingy
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 22:39:23 2020

@author: xingya
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def visit( l, r):
            nonlocal i
            
            if l == r:
                return 
            
            root_val = preorder[i]
            root = TreeNode(root_val)
            ind = d[root_val]

            i+=1
            root.left = visit(l, ind)
            root.right = visit(ind+1, r)
            return root
            
        i = 0
        d = {}
        for j in range(len(inorder)):
            d[inorder[j]] = j
                
        return visit(0, len(inorder))
            
class Test:
    def testBuildTree(self):
        preorder = [3,9,20,15,7]
        inorder = [9,3,15,20,7]
        
        s = Solution()
        # Build the Tree
        root = s.buildTree(preorder, inorder)
        
        output_inorder = self.inorder(root, [])
        output_preorder = self.preorder(root, [])
        
        print(output_inorder)
        print(output_preorder)
        
        assert output_inorder == inorder
        assert output_preorder == preorder
        
    def inorder(self, root, l):
        
        if root is not None:
            self.inorder(root.left,l)
            l.append(root.val)
            self.inorder(root.right,l)
            return l
        
    def preorder(self, root, l):
        
        q = [root]
        
        while q:
            node = q.pop()
            l.append(node.val)
            if node.left is not None:
                q.insert(0, node.left)
            if node.right is not None:
                q.insert(0, node.right)
        return l
                

t = Test()
t.testBuildTree()

"""
Runtime: 40 ms, faster than 99.97% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
Memory Usage: 18.8 MB, less than 7.13% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
"""
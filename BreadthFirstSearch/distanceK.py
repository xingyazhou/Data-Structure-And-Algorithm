# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 13:46:47 2020

@author: xingy
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 15:57:51 2020

863. All Nodes Distance K in Binary Tree (Medium)
We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.


Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.

Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
 
Note:

The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.

@author: xingya

Node: this algorithm is not originally designed by Xingya

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        self.dfs(root)
        
        if root:
        
            q = [(target, 0)]
            
            output = []
            seen = {target}
            
            while q:
                # Queue: FIFO                 
                if q[0][1] == K:
                    # Really smart Here! 
                    return [node.val for node, d in q]
                
                node, w = q.pop(0)
  
                for neb in (node.left, node.right, node.par):
                    if neb and neb not in seen:
                        
                        seen.add(neb)
                        q.append((neb, w+1))
                        
            return output
                               
    def dfs(self, node, par = None):
        if node:
            
            node.par = par
            self.dfs(node.left, node)   
            self.dfs(node.right, node)
            
            
class Test(object):
    def test(self):  
        root = TreeNode(3)
        root.left = TreeNode(5)
        root.left.left = TreeNode(6)
        root.left.right = TreeNode(2)
        root.left.right.left=TreeNode(7)
        root.left.right.right = TreeNode(4)
        
        root.right = TreeNode(1)
        root.right.left = TreeNode(0)
        root.right.right = TreeNode(8)
    
        s = Solution()
        output = s.distanceK(root, root.left, 2)
        
        expected = [7, 4, 1]
        
        assert (output == expected), "Wrong result, expected output is: [7, 4, 1]"
        print(output)
    
t = Test() 
t.test()

"""
Runtime: 20 ms, faster than 94.36% of Python online submissions for All Nodes Distance K in Binary Tree.
Memory Usage: 13.7 MB, less than 5.22% of Python online submissions for All Nodes
"""
    
    
    
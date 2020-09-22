# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 14:56:13 2020

257. Binary Tree Paths (Easy)

Given a binary tree, return all root-to-leaf paths.
Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3

@author: xingya

"""

# Definition for a binary tree node.

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        
        paths = []
        stack = [(root, str(root.val))]
        
        while stack:
            
            node, path = stack.pop()
            
            if not node.left and not node.right:
                paths.append(path)
                
            if node.left:
                stack.append((node.left, path + '->' + str(node.left.val)))
                
            if node.right:
                stack.append((node.right, path + '->' + str(node.right.val)))
        
        return paths
    
            
            
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)

s = Solution()
print(s.binaryTreePaths(root))

# Output
# ['1->3', '1->2->5']


"""
Runtime: 16 ms, faster than 89.85% of Python online submissions for Binary Tree Paths.
Memory Usage: 12.7 MB, less than 79.10% of Python online submissions for Binary Tree Paths.
"""

# Time complexity : O(N) since each node is visited exactly once.
# Space complexity : O(N) as we could keep up to the entire tree.

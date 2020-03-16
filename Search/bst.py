# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 20:30:46 2020

@author: xingya
"""

# definition of Binary Search Tree(BST) according to Wikipedia

# Binary Search Tree, is a node-based binary tree data structure which has the following properties:
# 1. The left subtree of a node contains only nodes with keys lesser than the node’s key.
# 2. The right subtree of a node contains only nodes with keys greater than the node’s key.
# 3. The left and right subtree each must also be a binary search tree.
# 4. There must be no duplicate nodes.


# node of BST   
class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.key = key 

# insert a new node         
def insert(root, node):
    # root is empty
    if root is None:
        root=node
        
    # insert node to the left of the BST
    elif root.key > node.key:      
        if root.left is None:
            root.left = node
        else:
            insert(root.left, node)
            
    # insert node to the right of the BST
    else:
        if root.right is None:
            root.right = node
        else:
            insert(root.right, node)

# inorder tree traversal :  from smallest element to largest element, keys in ascending order         
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key)
        inorder(root.right)

# Test bst        
r = Node(50) 
insert(r,Node(30)) 
insert(r,Node(20)) 
insert(r,Node(40)) 
insert(r,Node(70)) 
insert(r,Node(60)) 
insert(r,Node(80)) 

inorder(r)

# Output 
# 20
# 30
# 40
# 50
# 60
# 70
# 80
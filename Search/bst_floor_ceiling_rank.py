# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 20:30:46 2020

@author: xingya
"""

# definition of Binary Search Tree(BST) according to Wikipedia:
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
        self.count=1
        
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
        root.count += 1
            
    # insert node to the right of the BST
    else:
        if root.right is None:
            root.right = node
        else:
            insert(root.right, node)
        root.count += 1

# inorder tree traversal 
# from smallest element to largest element
# keys in ascending order         
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key)
        inorder(root.right)
               
# find the smallest element which is >= inp        
def ceiling(root, inp):
    # empty tree
    if root is None:
        return (-1)
    
    # found the case
    if root.key == inp:
        return (root.key)
   
    # root.key is smaller, traverse the right subtree
    if root.key < inp:
        return ceiling(root.right, inp)
    
    # root.key is larger, traverse the left subtree
    var = ceiling(root.left, inp)    
    return var if var >= inp else root.key

# find the largest element which is <= inp    
def floor(root, inp):
    # empty tree
    if root is None:
        return (-1)
    
    # found the case
    if root.key == inp:
        return (root.key)
    
    # root.key is bigger, traverse the left subtree
    if root.key > inp:
        return floor(root.left, inp)
    
    # root.key is smaller than inp, traverse the right subtree.
    var = floor(root.right, inp)    
    if var is not -1 and var <= inp:
        return (var)
    else:
        return (root.key)
    
# find number or elements in the bst that is < inp
def rank(root, inp):
    # empty tree
    if root:
        if root.key == inp:
            # root.left is not empty
            if root.left:
                return (root.left.count)
            # there is no chile in the root.left
            else:
                return 0
        
        # root.key is larger than inp, traverse the left subtree
        if root.key > inp:
            return rank(root.left, inp)
        
        # root.key is smaller than inp, traverse the right subtree
        if root.key < inp:
            if root.left:
                return (1 + root.left.count + rank(root.right, inp))
            else:
                return (1 + rank(root.right, inp))
    else:
        return 0
            
   
# Build BST    
root = Node(8)   
insert(root, Node(4) )
insert(root, Node(12) )
insert(root, Node(2) )
insert(root, Node(18) )
insert(root, Node(6) )
insert(root, Node(10) )
insert(root, Node(20) )
insert(root, Node(16) )
insert(root, Node(14) )

# Test insert, ceiling, floor, rank
print("i ceiling floor rank")   
for i in range(2,21): 
    print (i, "   ", ceiling(root, i), "   ", floor(root,i), "   ", rank(root, i))    

# Output
# i ceiling floor rank
# 2     2     2     0
# 3     4     2     1
# 4     4     4     1
# 5     6     4     2
# 6     6     6     2
# 7     8     6     3
# 8     8     8     3
# 9     10    8     4
# 10    10    10    4
# 11    12    10    5
# 12    12    12    5
# 13    14    12    6
# 14    14    14    6
# 15    16    14    7
# 16    16    16    7
# 17    18    16    8
# 18    18    18    8
# 19    20    18    9
# 20    20    20    9
        

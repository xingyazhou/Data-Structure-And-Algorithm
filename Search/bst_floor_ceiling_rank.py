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
        
        
# find the smallest element which is >= inp        
def ceiling(root, inp):
    if root is None:
        return (-1)
    
    if root.key == inp:
        return (root.key)
    
    if root.key < inp:
        return ceiling(root.right, inp)
    
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
    
    # root.key is bigger, traverse the left tree
    if root.key > inp:
        return floor(root.left, inp)
    
    # root.key is smaller than inp, traverse the right tree.
    var = floor(root.right, inp)    
    if var is not -1 and var <= inp:
        return (var)
    else:
        return (root.key)
    
    
# Build BST    
root = Node(8)   
root.left = Node(4) 
root.right = Node(12)  
root.left.left = Node(2) 
root.left.right = Node(6)   
root.right.left = Node(10) 
root.right.right = Node(14) 

# Test ceiling
print("ceiling:")   
for i in range(17): 
    print (i, ceiling(root, i))    

# Test floor    
print("\n\nfloor:")
for i in range(17):
    print(i, floor(root,i))
        
        
# Output   
     
#ceiling:
#0 2
#1 2
#2 2
#3 4
#4 4
#5 6
#6 6
#7 8
#8 8
#9 10
#10 10
#11 12
#12 12
#13 14
#14 14
#15 -1
#16 -1
#
#floor:
#0 -1
#1 -1
#2 2
#3 2
#4 4
#5 4
#6 6
#7 6
#8 8
#9 8
#10 10
#11 10
#12 12
#13 12
#14 14
#15 14
#16 14

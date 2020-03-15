# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 20:45:57 2020

@author: xingya
"""

# A Binary Heap is a Complete Binary Tree where items are stored in a special order 
# such that value in a parent node is greater(or smaller) than the values in its 
# two children nodes. The former is called as max heap and the latter is called min heap. 
# The heap can be represented by binary tree or array.



def heapify(a, n, i):
    
    # left child index = i * 2 +1
    # right child index = i* 2 +2
    l = i * 2 + 1
    r = i * 2 + 2
    
    # set root as largest
    largest = i
    
    # check if left child of root exist
    # check if the left child is larger than root
    if l < n and a[largest] <= a[l]:
        largest = l

    # check if right child of root exist
    # check if the right child is larger than root        
    if r < n and a[largest] <= a[r]:
        largest = r
        
    if i != largest :
        # swap
        a[i], a[largest] = a[largest], a[i]
        
        # heapify the largest index 
        heapify(a, n, largest)

def heapsort(a):
    
    n=len(a)
    
    # traverse the tree from bottom to root 
    # build a max heap
    for i in range(n-1, -1, -1):
        heapify(a, n, i)
     
    # extract the element from largest to smallest
    for j in range(n-1, 0, -1):
        a[j], a[0] = a[0], a[j]
        heapify(a, j, 0)
        
    return a        
        
    
a=[10,8,3,8.0,4,5,7]
print(heapsort(a))       
    
# Output [3, 4, 5, 7, 8, 8.0, 10]
# Stable
# time complexity O(2NlgN)

    
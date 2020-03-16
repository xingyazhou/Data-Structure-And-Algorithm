# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 21:37:35 2020

@author: xingya
"""

# This function takes last array element as pivot, all elements 
# smaller than pivot is placed at left position of pivot, all 
# elements larger than pivot is placed at right position of pivot


def quicksort(a, l, r):
    if l < r:
        # calculate pivot index
        # there is different ways to pick pivot, here we use a[r] as pivot
        pi = partition(a, l, r)

        quicksort(a, l, pi-1)
        quicksort(a, pi+1, r)
        
def partition(a, l, r):
    i= l-1
      
    for j in range(l, r):
        if a[j]< a[r]:
            i+=1
            # take a[r] as pivot, all elements from 0 to i is smaller than pivot, 
            # all elements from array position i+1 is larger than pivot
            a[i], a[j] = a[j], a[i]
            
    a[i+1], a[r] = a[r], a[i+1]
    
    return i+1

    
a=[10, 8, 3, 8.0, 4, 5, 7]
quicksort(a, 0, len(a)-1)
print (a)

# output [3, 4, 5, 7, 8.0, 8, 10]
# from the output results, we could see that quicksort is not stable since 8 and 8.0 is not in original order
# time complexity O(1.39NlgN)
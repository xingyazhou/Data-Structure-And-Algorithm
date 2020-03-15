# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 16:10:59 2020

@author: xingya
"""

def selectionsort(a):
    
    # traverse all the array elements except the last element
    for i in range(len(a)-1):
        
        minIndex=i
        
        # find smallest element in the remaining array
        for j in range(i+1, len(a)):
            if a[j] < a[minIndex]:
                minIndex=j
                
        # swap the smallest element with the first element in the remaining array
        a[minIndex],a[i] = a[i],a[minIndex]
        
    return a

a=[10,8,3,8.0,4,5,7]
print(selectionsort(a))

# output [3, 4, 5, 7, 8, 8.0, 10]
# stable
# time complexity O(N*N/2)
                
                
        
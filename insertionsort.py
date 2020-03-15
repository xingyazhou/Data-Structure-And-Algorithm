# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 13:53:14 2020

@author: xingya
"""

def insertionsort(a):
    
    for i in range(1, len(a)):
        j=i-1
        ref = a[i]
        
        # move all the elements larger than ref one position forward
        while j >= 0 and a[j] > ref :
            a[j+1] = a[j]
            j-=1
            
        a[j+1]=ref
        
    return a

a=[4,3,2,10,12,2.0,5,6]
print(insertionsort(a))

# output [2, 2.0, 3, 4, 5, 6, 10, 12]
# time complexity N*N/2
# Stable
            
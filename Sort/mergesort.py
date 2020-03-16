# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 15:39:00 2020

@author: xingya
"""

def mergesort(a):
    
    if len(a) >1:
        # find the middle index of the array
        m=len(a)//2
    
        # devide the array into two half arrays
        l=a[:m]
        r=a[m:]
    
        mergesort(l)
        mergesort(r)
        
        i=j=k=0
        
        # merge from two half arrays
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                a[k] = l[i]
                i+=1
                k+=1
            else:
                a[k] = r[j]
                j+=1
                k+=1
        
        # check if all the elements is merged
        while i < len(l):
            a[k]=l[i]
            k+=1
            i+=1
            
        while j < len(r):
            a[k]=r[j]
            k+=1
            j+=1
            
    return (a)


a=[4,3,2,10,12,2.0,5,6]
print(mergesort(a))

# output [2, 2.0, 3, 4, 5, 6, 10, 12]
# stable
# time complexity O(NlgN)
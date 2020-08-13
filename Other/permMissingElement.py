# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 21:20:27 2020

@author: xingy
"""

def permMissingElement(A):
    N = len(A)
    
    if N == 0:
        return 0
    
    if N == 1:
        return 3-  A[0]
        
    SUM = (1 + N +1) * (N + 1) / 2
    
    return int(SUM) - sum(A)
    
    
    
def sum(A):

    if len(A) == 1:
        return A[0]
    if len(A) >1:
        mi = len(A) // 2
        
        l = A[:mi]
        r = A[mi:]
        
        sum(l)
        sum(r)
        
        i=j=0
        s=0
        while i < len(l):
            s = s + l[i]
            i = i+1
        while j < len(r):
            s = s + r[j]
            j = j+1
        return s
  
        
        
A=[1,2,3,4,5,6,8,9,10,11,12,13]
print(permMissingElement(A))

# Output
# 7
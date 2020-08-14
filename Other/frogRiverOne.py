# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 23:40:30 2020

@author: xingy
"""

def frogRiverOne(X,A):
    
    if X > len(A):
        return -1
    
    count = [0] * (X+1)
    count[0]=1
    
    n = len(A)
    
    for t in range(n):
        count[A[t]]  = 1 + count[A[t]]
        
        if 0 not in count:
            return t
    return -1
        
A=[1,3,1,4,2,3,5,4]   
print(frogRiverOne(5,A))     
        
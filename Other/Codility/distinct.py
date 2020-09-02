# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 11:08:20 2020

Distinct
Compute number of distinct values in an array.

Write a function

def solution(A)

that, given an array A consisting of N integers, returns the number of distinct values in array A.

For example, given array A consisting of six elements such that:

 A[0] = 2    A[1] = 1    A[2] = 1
 A[3] = 2    A[4] = 3    A[5] = 1
the function should return 3, because there are 3 distinct values appearing in array A, namely 1, 2 and 3.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].

@author: xingya

"""

def distinct(A):
    
    if len(A)==0:
        return 0
    
    d={}
    
    for x in A:
        if x not in d:
            d[x] = "TRUE"
        
    return (len(d))
    
  

A=[1,2,3,3,2,4,5,7,7,4,4,2,2,1,99]
print(distinct(A))

# Output
# 7
        
        
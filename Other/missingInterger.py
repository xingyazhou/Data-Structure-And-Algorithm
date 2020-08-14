# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 20:36:23 2020

@author: xingy

MissingInteger
Find the smallest positive integer that does not occur in a given sequence.


Task description
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].

"""

def MissingInterger(A):
    
    t = [0] * 1000001
    
    t[0]=1
    
    for x in A:
        if x > 0:
            t[x] = t[x] + 1
            
    return ( t.index(0) )
    
A=[1,3,6,4,1,2]

print(MissingInterger(A))

# Output
# 5
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 11:49:08 2020

@author: xingy

CountDiv Task description

Write a function:

def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.

"""

def countDiv(A, B, K):
    if A == 0 and B == 0:
        return 1
    
    if K > B and A == 0:
        return 1
    
    if K > B:
        return 0
    
    if A % K == 0 :
        return (B // K - A // K + 1)
    else:
        return (B // K - A // K)
    
    
print(countDiv(6,11,2))

# Output
# 3
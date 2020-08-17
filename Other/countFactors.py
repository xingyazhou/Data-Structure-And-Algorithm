# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 12:19:50 2020

CountFactors
Count factors of given number n.

Task description
A positive integer D is a factor of a positive integer N if there exists an integer M such that N = D * M.

For example, 6 is a factor of 24, because M = 4 satisfies the above condition (24 = 6 * 4).

Write a function:

def solution(N)

that, given a positive integer N, returns the number of its factors.

For example, given N = 24, the function should return 8, because 24 has 8 factors, namely 1, 2, 3, 4, 6, 8, 12, 24. There are no other factors of 24.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].

@author: xingya
"""
import math

def CountFactors(N):
    
    if N == 1:
        return 1
    
    s = int(math.sqrt(N)) 
    count = 0
    
    for i in range(1, s+1):
        if N % i == 0:
            count +=2
            
    if s*s == N:
        count -= 1
        
    return count

print(CountFactors(16))

# Output
# 5
# time complexity: O(sqrt(N))
    
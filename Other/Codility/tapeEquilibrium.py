# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 22:51:58 2020
@author: xingy

Task description:  TapeEquilibrium

A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

For example, consider array A such that:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
We can split this tape in four places:

P = 1, difference = |3 − 10| = 7
P = 2, difference = |4 − 9| = 5
P = 3, difference = |6 − 7| = 1
P = 4, difference = |10 − 3| = 7
Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

For example, given:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−1,000..1,000].
"""

def TapeEquilibrium(A):
    if len(A) == 0 and len(A) == 1:
        return 0
    
    s = sum(A)
    maxdiff = abs(s - 2*A[0])
    s= s - 2*A[0]
    
    for i in range(1,len(A)-1):
        s = s - 2*A[i]
        
        if abs(s) < maxdiff:
            maxdiff = abs(s)
    return maxdiff
        
       
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
    
A= [3,1,2,4,3]
print(TapeEquilibrium(A))

# Output
# 1
# time complexity O(N)
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 23:10:13 2020

@author: xingy

PassingCars
Count the number of passing cars on the road.


Task description
A non-empty array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.

Array A contains only 0s and/or 1s:

0 represents a car traveling east,
1 represents a car traveling west.
The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.

For example, consider array A such that:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the number of pairs of passing cars.

The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.

For example, given:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer that can have one of the following values: 0, 1.

"""



def PassingCars(A):
    numOfOne = A.count(1)    
    numOfZero = A.count(0)
    
    result = 0
    
    if numOfOne == 0 or numOfZero==0:
        return 0
    
    if numOfZero > 0:
        posZero = GetPositions(0,A)
        l=posZero[0]
        numOfOne =numOfOne - A[0:l].count(1)     
        
        for r in posZero:
            numOfOne = numOfOne - A[l:r].count(1)
          
            result = result + numOfOne 
            l=r
    if result > 1000000000:
        return -1
         
    return result
     
def GetPositions(N,A):
     
    num = A.count(N) 
    
    l=[] 
        
    if num >0:
        pl = A.index(N)
        l.append(pl)
        num = num - 1
               
        while num > 0:
            pl = A.index(N, pl+1, len(A))             
            l.append(pl)              
            num = num - 1
            
    return l

A=[1,0,1,1,0,1,1,1,1]
print(PassingCars(A))

# Output
# 10
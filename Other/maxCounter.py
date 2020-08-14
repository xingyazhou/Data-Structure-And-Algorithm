# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 21:33:59 2020

@author: xingy

MaxCounters
Calculate the values of counters after applying all alternating operations: increase counter by 1; 
set value of all counters to current maximum.

Task description
You are given N counters, initially set to 0, and you have two possible operations on them:

increase(X) − counter X is increased by 1,
max counter − all counters are set to the maximum value of any counter.
A non-empty array A of M integers is given. This array represents consecutive operations:

if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.
For example, given integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the values of the counters after each consecutive operation will be:

    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
The goal is to calculate the value of every counter after all operations.

Write a function:

def solution(N, A)

that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.

Result array should be returned as an array of integers.

For example, given:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the function should return [3, 2, 2, 4, 2], as explained above.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..100,000];
each element of array A is an integer within the range [1..N + 1].

"""

def MaxCounters(N,A):
    
    pos= GetPositions(N,A)    
    maxi = 0
    counter = [0] * (N+1)
    
    if len(pos) > 0:
        l = 0
        
        for r in pos:
            d={}
            if l == 0:      
                B = A[l:r]         
            else:
                B=A[l+1: r]
                
            for x in B:
                if  x>=1 and x<=N:
                    if x in d:
                        d[x] = d[x] + 1
                    else:
                        d[x] = 1
                    
            if len(d) >0:   
                maxi = max(d.values()) + maxi
                print(maxi,d)
                
            l=r
            
        counter = [maxi] * (N+1)
        
        C = A[pos[-1] +1 : ]    
        for x in C:
            if x>=1 and x<=N:
                counter[x] = counter[x] + 1
                     
    else:
        for x in A:
            if x >=1 and x<= N:
                counter[x] = counter[x] +1
            
    return counter[1:]
            


def GetPositions(N,A):
     
    num = A.count(N+1) 
    
    l=[] 
        
    if num >0:
        pl = A.index(N+1)
        l.append(pl)
        num = num - 1
               
        while num > 0:
            pl = A.index(N+1, pl+1, len(A))             
            l.append(pl)              
            num = num - 1
            
    return l
    
            
A = [0,0,0,0,0]

print(MaxCounters(5,A))
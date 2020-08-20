# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 23:40:06 2020

EquiLeader
Find the index S such that the leaders of the sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N - 1] are the same.

Task description
A non-empty array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the elements of A.

An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

For example, given array A such that:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
we can find two equi leaders:

0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
The goal is to count the number of equi leaders.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the number of equi leaders.

For example, given:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
the function should return 2, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].

TBI
Performance 75%
Need to be improved later
large_range
1, 2, ..., N, length = ~100,000✘TIMEOUT ERROR
Killed. Hard limit reached: 6.000 sec.
1.6.000 sTIMEOUT ERROR, Killed. Hard limit reached: 6.000 sec.

@author: xingya

"""


def EquiLeader2(A):
    
    if len(A) < 2:
        return 0
    
    numOfEL = 0
    dr ={}
    dl = {}  
    
    for x in A:
        if x in dr:
            dr[x] += 1
        else:
            dr[x] = 1

    for y in A[:len(A)-1]:
        dr[y] -= 1
        if y in dl:
            dl[y] += 1
        else:
            dl[y] = 1
      
        #print(dl,dr)
        if max(dl.values()) > sum(dl.values()) /2 and max(dr.values()) > sum(dr.values()) /2:
            leaderl = list(dl.keys())[list(dl.values()).index(max(dl.values()))]
            leaderr = list(dr.keys())[list(dr.values()).index(max(dr.values()))]
            
            if leaderl == leaderr:
                numOfEL += 1
  
    return numOfEL

A = [4,3,4,4,4,2]

print(EquiLeader2(A))
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 23:08:14 2020

Nesting
Determine whether a given string of parentheses (single type) is properly nested.

Task description
A string S consisting of N characters is called properly nested if:

S is empty;
S has the form "(U)" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, string "(()(())())" is properly nested but string "())" isn't.

Write a function:

def solution(S)

that, given a string S consisting of N characters, returns 1 if string S is properly nested and 0 otherwise.

For example, given S = "(()(())())", the function should return 1 and given S = "())", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..1,000,000];
string S consists only of the characters "(" and/or ")".

@author: xingya
"""


def Nesting(S):
    
    if len(S) == 0 :
        return 1
    if len(S) % 2 != 0:
        return 0
    
    s1 = []
    s2 = []
    
    for x in S:
        s1.append(x)
    
    while len(s1)>0:
        d = s1.pop()
        
        if d == ")":
            s2.append("(")
        if d == "(":
            if len(s2) == 0:
                return 0
            else:
                s2.pop()
        
    if len(s2) != 0:
        return 0

    return 1
    
    
    
    

S = "(()(())())"
print(Nesting(S))

# Output
# 1
# time complexity:O(N)
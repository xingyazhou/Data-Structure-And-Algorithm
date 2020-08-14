# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 10:30:31 2020

@author: xingy


Task description: Brackets

A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

S is empty;
S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

def solution(S)

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..200,000];
string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".

"""

def brackets(s):
    if len(s) == 0:
        return 1
    
    d = { ')':'(', '}':'{', ']':'[' }
    
    stack1 = []
    stack2 = []
    
    for c in s:
        stack1.append(c)
        
 
    while stack1:
        p1 = stack1.pop()
       
        if p1 in d:
            stack2.append(d[p1])
     
        elif stack2 :
            p2 = stack2.pop()
            if p1 != p2:
                return 0
        else: 
            return 0
    
    if len(stack1)==0 and len(stack2)==0:
        return 1
    else:
        return 0
      
S = "{[()(())]}"
print(brackets(S))  

# Output
# 1 
    
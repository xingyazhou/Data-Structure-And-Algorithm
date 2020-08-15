# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 21:36:06 2020

@author: xingy
"""

def countingSort(A):
    
    output = [0] * 256   
    count = [0] * 256
    
    for x in A:
        count[ord(x)] += 1
        
    for d in range(1,len(count)):
        count[d] = count[d-1] + count[d]      
        
    for x in A:
        output[count[ord(x)]] = x
        count[ord(x)] -= 1
    
    
    return "".join(output[1:len(A)])

A = "geeksforgeeks"

print(countingSort(A))

# Output
# eeeefggkkors
# Time Complexity: O(n+k)
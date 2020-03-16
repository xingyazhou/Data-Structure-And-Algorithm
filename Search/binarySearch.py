# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 13:59:23 2020

@author: xingya
"""

# Returns index of i if i exist in arr, else return -1 

def binarySearch(arr, l, r, i):
    if r>=l :
        
        # find the index of the element in the middle sof the array
        mid = (l + r) // 2
           
        # find the element i
        if arr[mid] == i:
            return mid
        
        # if the element i is smaller than the middle element, it could be in the left subarray
        elif arr[mid] > i :
            return binarySearch(arr, l, mid - 1, i)
        
        # if the element i is larger than the middle element, it could be in the right subarray
        else:
            return binarySearch(arr, mid + 1, r, i)
            
    else:
        # element is not find in the array
        return -1
    
    
# test binarySearch(arr, l, r, i)   
arr = [ 2, 3, 4, 5, 10, 40, 55, 80] 
i = 10
print(binarySearch(arr, 0, len(arr)-1, i))

# Output : 4
# Time Complexity O(logN)
            
    
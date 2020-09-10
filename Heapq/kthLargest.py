# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 21:36:48 2020

Kth Largest Element in a Stream

Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, which contains initial elements from the stream. For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.

Example:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
Note:
You may assume that nums' length ≥ k-1 and k ≥ 1.

Note: this algorithm is not originally from xingya, while it's good to know how to use the heapq library

@author: xingya

"""

import heapq

class KthLargest(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.heap = nums
       
        heapq.heapify(self.heap)
    

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """        
        heapq.heappush(self.heap, val)
        
        # if heap size grows bigger than k, then remove
        while len(self.heap)> self.k:
            heapq.heappop(self.heap)
            
        return self.heap[0]

    
k = 3
arr = [4,5,8,2]  
kthLargest = KthLargest(k, arr )

print(kthLargest.add(3)) # return 4
print(kthLargest.add(5)) # return 5
print(kthLargest.add(10))# return 5
print(kthLargest.add(9)) # return 8
print(kthLargest.add(4)) # return 8
  
   
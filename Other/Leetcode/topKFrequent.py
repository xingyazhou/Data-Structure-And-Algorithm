# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 18:37:15 2020

Top K Frequent Elements
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.

@author: xingya

"""

from collections import defaultdict


def topKFrequent(nums, k):
    
    d=defaultdict(int)
    for x in nums:
        d[x] += 1

    d = sorted(d.items(), key=lambda kv: kv[1], reverse=True)
    
    r = []
    for x in range(k):
        r.append(d[x][0])

    return r
       
nums = [1,1,1,2,2,3,3,3,3]
k = 2
print(topKFrequent(nums, k))


# Output
# [3,1]

"""
Runtime: 92 ms, faster than 86.54% of Python online submissions for Top K Frequent Elements.
Memory Usage: 16.1 MB, less than 80.29% of Python online submissions for Top K Frequent Elements.
"""
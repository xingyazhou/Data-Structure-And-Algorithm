# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 14:00:43 2020

146. LRU Cache (Medium)
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
Follow up:
Could you do get and put in O(1) time complexity?

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:

1 <= capacity <= 3000
0 <= key <= 3000
0 <= value <= 104
At most 3 * 104 calls will be made to get and put.

Note: This algorithm is not originally designed by Xingya
@author: xingya

"""
from collections import OrderedDict

class LRUCache(OrderedDict):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return - 1
        
        self.cache.move_to_end(key)

        return self.cache[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            self.cache.move_to_end(key)
 
        self.cache[key] = value
        
        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)


s = LRUCache(2)

s.put(1,1)
s.put(2,2)
print(s.get(1))
s.put(3,3)
print(s.get(2))
s.put(4,4)
print(s.get(1))
print(s.get(3))
print(s.get(4))



"""
Runtime: 168 ms, faster than 99.61% of Python3 online submissions for LRU Cache.
Memory Usage: 23.1 MB, less than 48.70% of Python3 online submissions for LRU Cache.

"""










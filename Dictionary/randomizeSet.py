# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 11:39:58 2020

380. Insert Delete GetRandom O(1) (Medium)

Implement the RandomizedSet class:

bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
Follow up: Could you implement the functions of the class with each function works in average O(1) time?

Example 1:

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.

@author: xingya

This algorithm is not originally from Xingya.
"""

import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.l = []
        
        
    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.d:
            self.d[val] = len(self.l)
            self.l.append(val)
            return True
        
        return False
                 

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.d:
            return False
         
        i = self.d[val]
        lastelement = self.l[-1]
        
        self.d[lastelement] = i        
        self.l[i] = lastelement
        
        self.l.pop()
        del self.d[val]
        return True
        
    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
     
        return choice(self.l)
    

r = RandomizedSet()
print(r.insert(1))
print(r.remove(2))
print(r.insert(2))
print(r.getRandom())
print(r.remove(1))
print(r.insert(2))
print(r.getRandom())

# Output
# True
# False
# True
# 1
# True
# False
# 2


"""
Runtime: 84 ms, faster than 98.15% of Python online submissions for Insert Delete GetRandom O(1).
Memory Usage: 17.4 MB, less than 59.13% of Python online submissions for Insert Delete GetRandom O(1).
"""
    
    
    
        
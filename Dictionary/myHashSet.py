# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 10:42:12 2020

705. Design HashSet

Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

add(value): Insert a value into the HashSet. 
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

Example:

MyHashSet hashSet = new MyHashSet();
hashSet.add(1);         
hashSet.add(2);         
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);          
hashSet.contains(2);    // returns true
hashSet.remove(2);          
hashSet.contains(2);    // returns false (already removed)

Note:

All values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashSet library.

@author: xingya
"""

class Bucket():
    def __init__(self):
        self.bucket = []
        
    def add(self, k):
  
        found = False
        for i, key in enumerate(self.bucket):
            if k == key:
                found = True
                break
        if found == False:
            self.bucket.append(k)

            
    def remove(self, k):
        for i, key in enumerate(self.bucket):
            if k == key:
                del self.bucket[i]
                
    def contains(self, k):
        for key in self.bucket:
            if k == key:
                return True
        return False
            

class MyHashSet():

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyspace = 1023
        self.bucket = [Bucket() for i in range(self.keyspace)]
        
    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        k = key % self.keyspace
        self.bucket[k].add(key)
        
    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        k = key % self.keyspace
        self.bucket[k].remove(key)
        
    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        k = key % self.keyspace
        return self.bucket[k].contains(key)
        

hashSet = MyHashSet();
hashSet.add(1);         
hashSet.add(2);   
hashSet.add(1024);   
hashSet.add(2047);   
hashSet.add(2047); 
print(hashSet.contains(1));    
print(hashSet.contains(1024));  
print(hashSet.contains(1025)); 
hashSet.contains(3);  
hashSet.add(2);          
hashSet.contains(2);    
hashSet.remove(2);          
hashSet.contains(2);    

# Output
# True
# True
# False

"""
Runtime: 200 ms, faster than 71.24% of Python online submissions for Design HashSet.
Memory Usage: 17.7 MB, less than 67.43% of Python online submissions for Design HashSet.
"""

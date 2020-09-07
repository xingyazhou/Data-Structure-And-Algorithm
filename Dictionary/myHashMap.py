# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 10:09:34 2020

706. Design HashMap
Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

Example:

MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);          
hashMap.put(2, 2);         
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);          // update the existing value
hashMap.get(2);            // returns 1 
hashMap.remove(2);          // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found) 

Note:

All keys and values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashMap library.

Note: This algorithm is not originally designed by Xingya, learned from Solution

@author: xingya
"""

class Bucket():
    def __init__(self):
        self.bucket = []
        
    def get(self, k):
        for i, kv in enumerate(self.bucket):
            if k == kv[0]:
                return kv[1]          
        return -1
    
    def add(self, k,v):
        found = False
        for i, kv in enumerate(self.bucket):
            if k == kv[0]:
                self.bucket[i] = (k,v)
                found = True
        
        if found == False:
            self.bucket.append((k,v))
            
    def remove(self, k):
        for i,kv in enumerate(self.bucket):
            if k == kv[0]:
                self.bucket.remove((kv[0],kv[1]))
                # del self.bucket(i)
                       
class HashTable():
    def __init__(self):
        self.keyspace = 1023
        # self.bucket is nested list which means Bucket() is a list inside self.bucket
        self.bucket = [Bucket() for i in range(self.keyspace)]
        
    def get(self, k):
        key = k % self.keyspace      
        return self.bucket[key].get(k)
    
    def put(self, k, v):
        key = k % self.keyspace   
        self.bucket[key].add(k,v)
        
    def remove(self, k):
        key = k % self.keyspace
        self.bucket[key].remove(k)
        
 
hashMap = HashTable()
hashMap.put(1, 1)         
hashMap.put(1, 2)  
hashMap.put(1024, 1024)     
print(hashMap.get(1)  )  
print(hashMap.get(1024)  )        
print(hashMap.get(3)    )        
hashMap.put(2, 2)          
print(hashMap.get(2)   )       
hashMap.remove(2)        
print(hashMap.get(2)    )     
hashMap.put(7,3)   
print(hashMap.get(7))

# Output
# 2
# 1024
# -1
# 2
# -1
# 3

"""
Runtime: 236 ms, faster than 81.57% of Python online submissions for Design HashMap.
Memory Usage: 16.2 MB, less than 62.35% of Python online submissions for Design HashMap.
"""


      
    

            
            
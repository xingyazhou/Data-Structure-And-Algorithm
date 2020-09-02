# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 22:47:09 2020

@author: xingy
"""

import collections

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        count_t= collections.Counter(t)
        
        for k in count_t:
            print(s.count(k), k, count_t[k])
            if s.count(k) <  count_t[k]:
                return False
        return True
    
    
s = "anagram"
t = "nagaram"

c=Solution()
print(c.isAnagram(s,t))

# Output
# 1 n 1
# 3 a 3
# 1 g 1
# 1 r 1
# 1 m 1
# True
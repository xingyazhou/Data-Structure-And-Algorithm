# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 20:51:41 2020

@author: xingy
"""
from collections import defaultdict

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d=defaultdict(int)
        
        for i in s:
            d[i] += 1

        # find the index
        for idx, ch in enumerate(s):
            print(idx,ch)
            if d[ch] == 1:
                return idx     
        return -1


s="lleetcode"
solution=Solution()
k=solution.firstUniqChar(s)
print(k)
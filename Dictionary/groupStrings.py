# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 22:01:24 2020

Group Shifted Strings

Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of non-empty strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

Example:

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output: 
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]

@author: xingya

"""

from collections import defaultdict
class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]-
        """
       
        mydict = defaultdict(list)
        
        for s in strings:
            
            n=len(s)
            key = ''
            
            if n>1:
                for i in range(1,n):
                    
                    d = ord(s[i]) - ord(s[i-1])             
                    if d < 0:
                        d += 26
                    key+=str(d)
 
                mydict[key].append(s)
                
            if n == 1:
                mydict[0].append(s)
                
               
        return (list(mydict.values()))
        

input = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
s = Solution()
print(s.groupStrings(input))


# Output
# [['abc', 'bcd', 'xyz'], ['acef'], ['az', 'ba'], ['a', 'z']]


"""
23 / 23 test cases passed.
Status: Accepted
Runtime: 28 ms
Memory Usage: 12.8 MB

Your runtime beats 54.55 % of python submissions.
Your memory usage beats 46.54 % of python submissions.

"""
                
                
                





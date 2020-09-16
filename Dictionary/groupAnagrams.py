# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 15:12:25 2020

49. Group Anagrams (Medium)
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 
Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.

@author: xingya
"""


from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """     

        d = defaultdict(list)
        
        for str in strs:
            key = ''.join(sorted(str))          
            d[key].append(str)
            
        return list(d.values())
    




      
#strs =["ddddddddddg","dgggggggggg"] 
strs=["eat","tea","tan","ate","nat","bat"]            
s = Solution()
print(s.groupAnagrams(strs))


# Output
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    
"""
Runtime: 72 ms, faster than 99.79% of Python online submissions for Group Anagrams.
Memory Usage: 16.6 MB, less than 72.40% of Python online submissions for Group Anagrams.
"""
        


# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 13:48:17 2020

383. Ransom Note
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

You may assume that both strings contain only lowercase letters.

@author: xingya
"""


from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote, magazine):
        
        d= defaultdict(int)
        
        for x in magazine:
            d[x] += 1
            
        for y in ransomNote:
            d[y] -= 1
        
            if d[y] < 0:
                return False
            
        return True
    
ransomNote = "a"
magazine = "b"
s = Solution()
print(s.canConstruct(ransomNote, magazine))

ransomNote = "aa"
magazine = "aab"
print(s.canConstruct(ransomNote, magazine))


# Output 
# False
# True 

"""  
Runtime: 64 ms, faster than 55.33% of Python3 online submissions for Ransom Note.
Memory Usage: 13.7 MB, less than 99.19% of Python3 online submissions for Ransom Note.      
""" 

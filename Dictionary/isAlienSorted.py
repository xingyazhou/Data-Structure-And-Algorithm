# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 20:49:31 2020
953. Verifying an Alien Dictionary (Easy)

Share
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.


Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

@author: xingya
"""

from collections import defaultdict
import unittest

class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """        
        d = defaultdict(int)
        
        for i, c in enumerate(order):
            d[c] = i
        
        for i in range(1, len(words)):
            
            w1 = words[i-1]
            w2 = words[i]
            flag = False
            n = min(len(w1), len(w2))
            
            # compare w1 and w2
            for j in range(n):
                if d[w1[j]] < d[w2[j]]:
                    flag = True
                    break
                    
                if d[w1[j]] > d[w2[j]]:
                    return False
                
            if len(w1) > len(w2) and flag == False:
                return False
            
        return True
        

class Test(unittest.TestCase):
    def testIsAlienSorted(self):
        
        print("\n\nStarting Test isAlienSorted ...")
        
        words1 = ["fxasxpc","dfbdrifhp","nwzgs","cmwqriv","ebulyfyve","miracx","sxckdwzv","dtijzluhts","wwbmnge","qmjwymmyox"]
        order1 = "zkgwaverfimqxbnctdplsjyohu"  
        expected1 = False
        
        words2 = ["hello","leetcode"] 
        order2 = "hlabcdefgijkmnopqrstuvwxyz"
        expected2 = True
        
        s = Solution()
        output1 = s.isAlienSorted(words1, order1)
        output2 = s.isAlienSorted(words2, order2)
        
        print(output1, output2)
        assert output1 == expected1
        assert output2 == expected2
    
    
if __name__ == '__main__':
    unittest.main()

"""
Runtime: 28 ms, faster than 96.14% of Python3 online submissions for Verifying an Alien Dictionary.
Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Verifying an Alien Dictionary.
"""
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 12:13:22 2020

17. Letter Combinations of a Phone Number (Medium)
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]

@author: xingya

"""
import unittest

class Solution:
    
    d = {
     '2': ['a', 'b', 'c'], 
     '3': ['d', 'e', 'f'], 
     '4': ['g', 'h', 'i'], 
     '5': ['j', 'k', 'l'],
     '6': ['m', 'n', 'o'], 
     '7': ['p', 'q', 'r', 's'], 
     '8': ['t', 'u', 'v'], 
     '9': ['w', 'x', 'y','z']
     }
    
    def letterCombinations(self, digits):
        
        stack = []
        for x in digits:
            stack.append(x)
            
        res = []
        while stack:
            i = stack.pop()

            if len(res) == 0:
                for e in d[i]:
                    res.append(e)
                    
            else:
                
                temp = []
                for j in range(len(res)):               
                    for e in d[i]:
                        temp.append( e + res[j] )
                
                res = []
                for x in temp:
                    res.append(x)

        return res
    
                    
class Test(unittest.TestCase):
    def testLetterCombinations(self):
        print("\n\nStart testing letterCombinations ...\n")
        
        digits = '2345'     
        expected = ['adgj', 'bdgj', 'cdgj', 'aegj', 'begj', 'cegj', 'afgj', 'bfgj', 'cfgj', 
                    'adhj', 'bdhj', 'cdhj', 'aehj', 'behj', 'cehj', 'afhj', 'bfhj', 'cfhj', 
                    'adij', 'bdij', 'cdij', 'aeij', 'beij', 'ceij', 'afij', 'bfij', 'cfij', 
                    'adgk', 'bdgk', 'cdgk', 'aegk', 'begk', 'cegk', 'afgk', 'bfgk', 'cfgk', 
                    'adhk', 'bdhk', 'cdhk', 'aehk', 'behk', 'cehk', 'afhk', 'bfhk', 'cfhk', 
                    'adik', 'bdik', 'cdik', 'aeik', 'beik', 'ceik', 'afik', 'bfik', 'cfik', 
                    'adgl', 'bdgl', 'cdgl', 'aegl', 'begl', 'cegl', 'afgl', 'bfgl', 'cfgl', 
                    'adhl', 'bdhl', 'cdhl', 'aehl', 'behl', 'cehl', 'afhl', 'bfhl', 'cfhl', 
                    'adil', 'bdil', 'cdil', 'aeil', 'beil', 'ceil', 'afil', 'bfil', 'cfil']
        
        s = Solution()
        output = s.letterCombinations(digits)
        
        print(output)
        assert output == expected

if __name__ == '__main__':
    unittest.main()


"""
Runtime: 20 ms, faster than 98.81% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 14.1 MB, less than 99.98% of Python3 online submissions for Letter Combinations of a Phone Number.
"""


                    
                
            
        
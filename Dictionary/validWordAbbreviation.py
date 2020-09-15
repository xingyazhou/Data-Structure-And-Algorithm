# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 22:22:22 2020


288. Unique Word Abbreviation (Medium)
An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

     1
     ↓
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
     ↓   ↓    ↓    ↓  ↓    
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
     ↓   ↓    ↓
d) l|ocalizatio|n          --> l10n

Additionally for any string s of size less than or equal to 2 their abbreviation is the same string s.
Find whether its abbreviation is unique in the dictionary. A word's abbreviation is called unique if any of the following conditions is met:

There is no word in dictionary such that their abbreviation is equal to the abbreviation of word.
Else, for all words in dictionary such that their abbreviation is equal to the abbreviation of word those words are equal to word.
 

Example 1:

Input
["ValidWordAbbr","isUnique","isUnique","isUnique","isUnique"]
[[["deer","door","cake","card"]],["dear"],["cart"],["cane"],["make"]]
Output
[null,false,true,false,true]

Explanation
ValidWordAbbr validWordAbbr = new ValidWordAbbr(["deer", "door", "cake", "card"]);
validWordAbbr.isUnique("dear"); // return False
validWordAbbr.isUnique("cart"); // return True
validWordAbbr.isUnique("cane"); // return False
validWordAbbr.isUnique("make"); // return True
 

Constraints:

Each word will only consist of lowercase English characters.

@author: xingya

"""


from collections import defaultdict

class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.dict = defaultdict(list)
        
        for x in dictionary:
            
            if len(x) >2 :
                key = x[0] + str(len(x)-2) + x[-1]
                
                if x not in self.dict[key]:
                    self.dict[key].append(x)
                

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) <=2:
            return True
            
        else:
            key = word[0] + str(len(word) - 2) + word[-1]
            if key in self.dict:
                
                if len(self.dict[key]) >= 2:
                    return False
                
                elif self.dict[key][0] != word:
                    return False
                          
            return True
            
            
            
v= ValidWordAbbr(["deer", "door", "cake", "card"])

print(v.isUnique("dear"))
print(v.isUnique("cart"))
print(v.isUnique("cane"))
print(v.isUnique("make"))

# Output
# False
# True
# False
# True
               
                
"""        
Runtime: 196 ms, faster than 85.19% of Python online submissions for Unique Word Abbreviation.
Memory Usage: 26.8 MB, less than 85.19% of Python online submissions for Unique Word Abbreviation.   
"""   
        
        
        
        
        

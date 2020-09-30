# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 23:38:22 2020

Write a function that can take a string and return a list of bigrams.

Example:

sentence = 
""
Have free hours and love children? 
Drive kids to school, soccer practice 
and other activities.
""

output = [('have', 'free'),
 ('free', 'hours'),
 ('hours', 'and'),
 ('and', 'love'),
 ('love', 'children?'),
 ('children?', 'drive'),
 ('drive', 'kids'),
 ('kids', 'to'),
 ('to', 'school,'),
 ('school,', 'soccer'),
 ('soccer', 'practice'),
 ('practice', 'and'),
 ('and', 'other'),
 ('other', 'activities.')]


@author: xingya

"""

class Solution():
    def bigrams(self, sentence):
        if len(sentence) == 0:
            return []
        
        l = sentence.split(" ")
        output = []
        for i in range(1, len(l)):
            output.append((l[i-1].lower(), l[i].lower()))
        
        return output
        
    
class Test():
    def testBigrams(self):
        sentence = "Have free hours and love children? Drive kids to school, soccer practice and other activities."
        output = [   
                     ('have', 'free'),
                     ('free', 'hours'),
                     ('hours', 'and'),
                     ('and', 'love'),
                     ('love', 'children?'),
                     ('children?', 'drive'),
                     ('drive', 'kids'),
                     ('kids', 'to'),
                     ('to', 'school,'),
                     ('school,', 'soccer'),
                     ('soccer', 'practice'),
                     ('practice', 'and'),
                     ('and', 'other'),
                     ('other', 'activities.')
                ]
        
        s = Solution()
        bigram = s.bigrams(sentence)
        
        print(bigram)
        assert bigram == output
        
      
t = Test()
t.testBigrams()        
        
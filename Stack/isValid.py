# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 17:27:49 2020

20. Valid Parentheses (Easy)

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

@author: xingya
"""

class Solution:
    def isValid(self, s) :     
     
        d = {')':'(', '}': '{', ']': '['}
        stack = []
        
        for c in s:
         
            if c not in d:
                stack.append(c)
            
            else:
                if not stack:
                    return False
                      
                x = stack.pop()
                if x != d[c]:
                    return False
       
        return len(stack)==0
        
class Test:
    def test(self):
        s1 = "{[]}"
        s2 = "([)]"
        
        expected1 = True
        expected2 = False
        
        t = Solution()
        output1 = t.isValid(s1)
        output2 = t.isValid(s2)
        
        assert (output1 == expected1), "Wrong result, expected output is : True"
        assert (output2 == expected2), "Wrong result, expected output is : False"
        
        print(output1)
        print(output2)
        
t = Test()
t.test()

"""
Runtime: 12 ms, faster than 98.29% of Python online submissions for Valid Parentheses.
Memory Usage: 13.5 MB, less than 5.01% of Python online submissions for Valid Parentheses.   
"""         
                
    

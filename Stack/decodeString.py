# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 11:20:46 2020

394. Decode String (Medium)

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"

@author: xingya

"""

class Solution(object):    
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []  
        m = ""
        d=""
        
        for c in s:
 
            if c != ']':
                # c is digits 0-9
                if 48<= (ord(c)) <=57:
                    d += c
                    
                else:
                    if d!="":
                        stack.append(d)
                        d=""
                        
                    stack.append(c)
            else:
            # c is "]", pop element from stack until '['
                while stack:
                  
                    x = stack.pop()
                    
                    if x !='[':
                        m = x+m
                        
                    elif x=='[':
                        
                        num=int(stack.pop())     
                        m = m * num
                       
                        # Push the string m back to stack
                        stack.append( m )
                        m = ""
                        break
                    
        while stack:
            m = stack.pop()  + m          
        return m
    
                    
s = "3[a2[c]]" 
so = Solution()
print(so.decodeString(s) )            

s = "2[abc]3[cd]ef"
so = Solution()
print(so.decodeString(s) )

s = "abc3[cd]xyz"
so = Solution()
print(so.decodeString(s) )


"""
Runtime: 8 ms, faster than 99.55% of Python online submissions for Decode String.
Memory Usage: 12.7 MB, less than 63.94% of Python online submissions for Decode String

"""
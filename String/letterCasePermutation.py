# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 12:13:16 2020

784. Letter Case Permutation (Medium)
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.
Return a list of all possible strings we could create. You can return the output in any order.

Example 1:

Input: S = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: S = "3z4"
Output: ["3z4","3Z4"]
Example 3:

Input: S = "12345"
Output: ["12345"]
Example 4:

Input: S = "0"
Output: ["0"]
 
Constraints:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.

@author: xingya

"""

class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        output = []
        
        for c in S:

            if c.isalpha():
                l = []
                
                if len(output) == 0:
                    output.append(c.capitalize())
                    output.append(c.lower())
               
                else:
                    for x in output:
                        
                        l.append(x+c.capitalize())
                        l.append(x+c.lower())

                if l!=[]:
                    output=l
                    
            else:
                if len(output) == 0:
                    output.append(c)
                    
                else:
                    for i in range(len(output)):
                        output[i] += c
                    
        return output
    
class Test(object):
    def test(self):
        s=  "a1b2"
        solution = Solution()
        
        output = solution.letterCasePermutation(s)
        expected = ['A1B2', 'A1b2', 'a1B2', 'a1b2']
        
        assert (output == expected), "Wrong output, expected output is : ['A1B2', 'A1b2', 'a1B2', 'a1b2']"
        print(output)
        
        
t = Test()
t.test()


"""
Runtime: 32 ms, faster than 98.79% of Python online submissions for Letter Case Permutation.
Memory Usage: 14.2 MB, less than 33.17% of Python online submissions for Letter Case
"""
                    
                    
                    
            
        
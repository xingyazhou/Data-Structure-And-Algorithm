# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 15:05:09 2020

1100. Find K-Length Substrings With No Repeated Characters (Medium)
Given a string S, return the number of substrings of length K with no repeated characters.

Example 1:

Input: S = "havefunonleetcode", K = 5
Output: 6
Explanation: 
There are 6 substrings they are : 'havef','avefu','vefun','efuno','etcod','tcode'.
Example 2:

Input: S = "home", K = 5
Output: 0
Explanation: 
Notice K can be larger than the length of S. In this case is not possible to find any substring.

Note:

1 <= S.length <= 10^4
All characters of S are lowercase English letters.
1 <= K <= 10^4

@author: xingya
"""

class Solution(object):
    def numKLenSubstrNoRepeats(self, s, k):
        """
        :type S: str
        :type K: int
        :rtype: int
        """
        if len(s) < k:
            return 0
        
        l, r = 0, 0
        subs = set()
        output = 0
        
        for r in range(len(s)):
 
            if s[r] in subs:
                #print(r, s[r], subs)
                ind = s[l:r].index(s[r]) + l
                
                for j in range(l, ind):
                    subs.remove(s[j])
                    
                l = ind + 1
                
            if s[r] not in subs:
                subs.add(s[r])           
            
            if len(subs) == k:
                output += 1
                subs.remove(s[l])
                l += 1
                            
        return output

class Test(object):
    def test(self):

        s1 = "havefunonleetcode"
        k1 = 5
        
        s2 = "abab"
        k2 = 2
        
        expected1 = 6
        expected2 = 3
        
        s = Solution()
        output1 = s.numKLenSubstrNoRepeats(s1, k1)
        output2 = s.numKLenSubstrNoRepeats(s2, k2)
        
        print(output1)
        print(output2)
        
        assert (output1 == expected1), "Wrong result, expected output is : 5"
        assert (output2 == expected2), "Wrong result, expected output is : 3"
        
        
    
# Test
t = Test()
t.test()

"""
Runtime: 36 ms, faster than 100.00% of Python3 online submissions for Find K-Length Substrings With No Repeated Characters.
Memory Usage: 14.2 MB, less than 5.51% of Python3 online submissions for Find K-Length Substrings With No Repeated Characters.
"""





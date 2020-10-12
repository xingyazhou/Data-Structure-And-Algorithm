# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 13:28:50 2020

143. Longest Common Subsequence (Medium)

Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

If there is no common subsequence, return 0.
Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length <= 1000
1 <= text2.length <= 1000
The input strings consist of lowercase English characters only.

@author: xingya

"""

# Note: this algorithem is not originally created by Xingya
# https://leetcode.com/problems/longest-common-subsequence/solution/



from collections import defaultdict
class Solution:
    def longestCommonSubsequence(self, text1, text2):
        
        dp_grid = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        

        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
             
                if text1[i] == text2[j]: 
                    
                    dp_grid[i][j] = dp_grid[i+1][j+1] + 1
                    
                else:
                    dp_grid[i][j] = max(dp_grid[i][j+1], dp_grid[i+1][j])
                    
        return dp_grid[0][0]
        
        
class Test:
    def testLongestCommonSubsequence(self):
        
        text1 = "mhunuzqrkzsnidwbun"
        text2 = "szulspmhwpazoxijwbq"
        
        expected = 6
        
        s = Solution()
        output = s.longestCommonSubsequence(text1, text2)
        
        print(output)
        assert output == expected, "Wrong result, expected resutl is : 6"
        
        
t = Test()
t.testLongestCommonSubsequence()

"""
Runtime: 344 ms, faster than 96.13% of Python3 online submissions for Longest Common Subsequence.
Memory Usage: 21.7 MB, less than 5.22% of Python3 online submissions for Longest Common Subsequence.
"""
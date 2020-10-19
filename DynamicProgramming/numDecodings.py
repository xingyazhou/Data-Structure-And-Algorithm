# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 23:25:22 2020
91. Decode Ways (Medium)
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

@author: xingya
"""

import unittest

class Solution:
    
    def numDecodings(self, s):
        if len(s) == 0 or s[0] == '0':
            return 0
        
        if len(s) == 1 and s[0] != '0':
            return 1
        
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 0 if s[1] == '0' else 1

        for i in range(2, len(s)+1):
            
            dp[i] = dp[i-1]
            res = int(s[i-2:i])
            
            if  26 >= res >= 10:
                dp[i] += dp[i-2]
    
        return dp[-1]
                
        
class Test(unittest.TestCase):
    def testNumDecodings(self):
        
        s="226"
        expected = 3
        
        so = Solution()
        output = so.numDecodings(s)
            
        print("\nThe number of decoding ways: ", output)
        assert output == expected
        
if __name__ == '__main__':
    unittest.main()
    

"""
Runtime: 24 ms, faster than 97.20% of Python3 online submissions for Decode Ways.
Memory Usage: 14.1 MB, less than 7.16% of Python3 online submissions for Decode Ways.
"""
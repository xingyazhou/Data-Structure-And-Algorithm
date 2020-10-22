# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 23:33:27 2020

1189. Maximum Number of Balloons (Easy)
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:

Input: text = "nlaebolko"
Output: 1
Example 2:


Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0
 
Constraints:

1 <= text.length <= 10^4
text consists of lower case English letters only.

@author: xingya

"""
from collections import defaultdict
import sys
import unittest

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        dt = defaultdict(int)      
        for x in text:
            dt[x] += 1
        
        db = defaultdict(int)
        for x in 'balloon':
                db[x] += 1
        
        n = sys.maxsize
        for k, v in db.items():
            if k not in dt:
                return 0
            else:
                n = min(n, dt[k]//db[k])
                
        return n
                


class Test(unittest.TestCase):
    def testMaxNumberOfBalloons(self):
        text = "loonbalxballpoon"
        expected = 2
        
        s = Solution()
        output = s.maxNumberOfBalloons(text)
        
        print("\nThe maximum number of instances that can be formed :", output)
        assert output == expected
        

if __name__ == '__main__':
    unittest.main()


"""
Runtime: 24 ms, faster than 97.67% of Python3 online submissions for Maximum Number of Balloons.
Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Maximum Number of Balloons.
"""
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 23:07:23 2020

1002. Find Common Characters (Easy)
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  
For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]

Note:

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter

@author: xingya

"""
from collections import Counter
import unittest

class Solution:
    
    def commonChars(self, A) :
        
        r = []
        for x in A:
            r.append(dict(Counter(x)))
       
        output = []
        for k in r[0]:
            flag = 1
            n = r[0][k]
            
            for d in r[1:]:                
                if k not in d:
                    flag = 0
                else:
                    n = min(n, d[k])
                    
            if flag == 1:
                for i in range(n):
                    output.append(k)
                            
        return output
        
                        
class Test(unittest.TestCase):
    def testCommonChars(self):
        A = ["bella","label","roller"]  
        expected = ['e', 'l', 'l']
        
        s = Solution()
        output = s.commonChars(A)   
        
        print('\nCommon Characters: ', output)
        assert output == expected


if __name__ == '__main__':
    unittest.main()


"""
Runtime: 40 ms, faster than 94.28% of Python3 online submissions for Find Common Characters.
Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Find Common Characters.  
"""

 
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 20:28:06 2020

1207. Unique Number of Occurrences (Easy)

Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000

@author: xingya
"""

from collections import defaultdict
import unittest

class Solution:
    def uniqueOccurrences(self, arr):
        
        d = defaultdict(int)
        
        for x in arr:
            d[x] += 1
            
        s = set()
        for c in d.values():
            if c in s:
                return False
            else:
                s.add(c)
                
        return True

class Test(unittest.TestCase):
    def testUniqueOccurrences(self):
        print("\n\nTesting uniqueOccurrences ...")
    
        arr1 = [1,2,2,1,1,3]
        expected1 = True
        
        arr2 = [1,2]
        expected2 = False
        
        s = Solution()
        output1 = s.uniqueOccurrences(arr1)
        output2 = s.uniqueOccurrences(arr2)
        
        print(output1)
        print(output2)
        assert output1 == expected1
        assert output2 == expected2

if __name__ == "__main__":
    unittest.main()


"""
Runtime: 28 ms, faster than 95.48% of Python3 online submissions for Unique Number of Occurrences.
Memory Usage: 14.3 MB, less than 54.14% of Python3 online submissions for Unique Number of Occurrences.
"""
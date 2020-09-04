# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 15:07:28 2020

744. Find Smallest Letter Greater Than Target

Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"
Note:
letters has a length in range [2, 10000].
letters consists of lowercase letters, and contains at least 2 unique letters.
target is a lowercase letter.

@author: xingya
"""

# find smallest letter greater than target
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        return ceiling(letters, 0, len(letters)-1,target)

# binary search algorithm is used            
def ceiling(numbers, l, r, target):
    
    if l <= r:
        mi = (l+r) // 2

        if target >=numbers[-1]:
            return numbers[0]
                      
        if numbers[mi] <= target :
            return ceiling(numbers, mi+1, r, target)
        
        f = numbers[mi]             
        r = ceiling(numbers, l, mi-1, target)
 
        if r is not None and r<f:
            return r
        
        return f
        
        
letters = ["c", "f", "j"]
target = "j"
s=Solution()
print(s.nextGreatestLetter(letters, target))

# Output
# c

"""
Runtime: 76 ms, faster than 99.01% of Python online submissions for Find Smallest Letter Greater Than Target.
Memory Usage: 14.5 MB, less than 91.87% of Python online submissions for Find Smallest Letter Greater Than Target.
"""
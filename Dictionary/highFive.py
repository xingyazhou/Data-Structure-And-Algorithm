# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 21:40:03 2020

1086. High Five (Easy)
Given a list of scores of different students, return the average score of each student's top five scores in the order of each student's id.

Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.  The average score is calculated using integer division.

Example 1:

Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation: 
The average of the student with id = 1 is 87.
The average of the student with id = 2 is 88.6. But with integer division their average converts to 88.

Note:

1 <= items.length <= 1000
items[i].length == 2
The IDs of the students is between 1 to 1000
The score of the students is between 1 to 100
For each student, there are at least 5 scores

@author: xingya

"""

from collections import defaultdict
import unittest

class Solution:
    def highFive(self, items):
        
        d = defaultdict(list)
        output = []
        
        for item in items:
            id = item[0]
            score = item[1]
            
            ## could be improved not to save all score while only top five.
            d[id].append(score)
            
        for id in d:
            d[id].sort(reverse = True)
            l = d[id][:5]
            output.append([id, sum(l) // len(l)])
  
        return output
                
class Test(unittest.TestCase):
    def testHighFive(self):
        print("\n\nStart Testing hightFive ...")
        items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
        expected = [[1,87],[2,88]]
        
        s = Solution()
        output = s.highFive(items)
        
        print(output)
        assert(output == expected)
        

if __name__ == '__main__':
    unittest.main()

"""
Runtime: 40 ms, faster than 100.00% of Python online submissions for High Five.
Memory Usage: 14 MB, less than 53.20% of Python online submissions for High Five.
"""
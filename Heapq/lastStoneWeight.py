# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 22:00:27 2020

1046. Last Stone Weight (Easy)

We have a collection of stones, each stone has a positive integer weight.
Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
 
Note:

1 <= stones.length <= 30
1 <= stones[i] <= 1000

@author: xingya

"""

import heapq
import unittest

class Solution:
    def lastStoneWeight(self, stones):
     
        h = []
        for x in stones:
            heapq.heappush(h, x)
            
        while len(h) >= 2:
            
            y, x = heapq.nlargest(2, h)
            
            if x != y:
                heapq.heappush(h, y-x)
                
            h.remove(x)
            h.remove(y)
                
        if len(h) == 1:
            return h[0]
        else:
            return 0
        

class Test(unittest.TestCase):
    def testLastStoneWeight(self):
        
        print("\n\nTesting lastStoneWeight ...")
        
        stones1 = [2,7,4,1,8,1]
        expected1 = 1
        
        stones2 =  [2,7,4,1,8,1, 1]
        expected2 = 0
        
        s = Solution()
        output1 = s.lastStoneWeight(stones1)
        output2 = s.lastStoneWeight(stones2)
        
        print("Input:", stones1, " Output:", output1)
        print("Input:", stones2, " Output:", output2)
        assert output1 == expected1
        assert output2 == expected2
        
if __name__ == "__main__":
    unittest.main()
              
        
"""        
Runtime: 28 ms, faster than 82.03% of Python3 online submissions for Last Stone Weight.
Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Last Stone Weight.
"""
        
        
        
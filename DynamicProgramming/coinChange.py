# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 14:45:24 2020

322. Coin Change (Medium)
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
Example 4:

Input: coins = [1], amount = 1
Output: 1
Example 5:

Input: coins = [1], amount = 2
Output: 2
 
Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 231 - 1

@author: xingya

"""


import sys

class Solution(object):
    def coinChange(self, coins, amount) :
        """
        Dynamic programming - Bottom up
        Before calculating F(i), we have to compute all minimum counts for amounts up to i
        """    
        F = [sys.maxsize] * (amount + 1 )
        F[0] = 0
        
        for i in range(1, amount+1):
            
            for c in coins:
                
                if i - c >= 0:
                    F[i] = min(F[i], F[i-c] + 1)
        
        if F[-1] == sys.maxsize:
            return -1
        else:
            return F[-1]
             

class Test(object):
    def test(self):
        
        s = Solution()
        coins1 = [1,2,5]
        amount1 = 11
        expected1 = 3
        
        
        coins2 =[2]
        amount2 = 3
        expected2= -1
        
        output1 = s.coinChange(coins1, amount1)
        output2 = s.coinChange(coins2, amount2)
        
        assert (output1 == expected1), "Wrong result, expected output: 3"
        assert (output2 == expected2), "Wrong result, expected output: -1"
        
        print(output1)
        print(output2)

t = Test()
t.test()


# Time complexity : O(S*n)
# Space complexity : O(S)

"""
Runtime: 1128 ms, faster than 62.79% of Python online submissions for Coin Change.
Memory Usage: 13.7 MB, less than 25.11% of Python online submissions for Coin Change.
"""
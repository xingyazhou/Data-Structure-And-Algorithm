# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 19:14:19 2020

121. Best Time to Buy and Sell Stock (Easy)
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

@author: xingya
"""

class Solution:
    def maxProfit(self, prices):
        
        if len(prices) == 0:
            return 0 
        
        minPrice = prices[0]
        maxProfits = 0
        
        for i in range(1, len(prices)):
            currentProfits = prices[i] - minPrice
            maxProfits = max(maxProfits, currentProfits)
            minPrice = min(minPrice, prices[i])
  
        return maxProfits
    
                
prices = [7,1,5,3,6,4]
s = Solution()
print(s.maxProfit(prices))  

# Output
# 5


# Time complexity : O(n)
# Space complexity : O(1)

"""
Runtime: 52 ms, faster than 99.16% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 14.8 MB, less than 98.79% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""
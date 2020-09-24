# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:34:17 2020

692. Top K Frequent Words (Medium)

Share
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.

@author: xingya

"""


import heapq
from collections import defaultdict

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """  
        d = defaultdict(int)
        for word in words:
            d[word] += 1
        
        heap = []
        for word, count in d.items():
            heappush(heap, (-count, word))
                
        output = []
        for _ in range(k):
            output.append(heapq.heappop(heap)[1])
            
        return output       
        
class Test(object):
    def test_topKFrequent(self):
        
        words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
        k = 4
        
        s = Solution()
        output = s.topKFrequent(words, k)
        expected = ['the', 'is', 'sunny', 'day']
        assert (output == expected), "Wrong Output, expected result is : ['the', 'is', 'sunny', 'day']"
        
        print(output)
 
t = Test()
t.test_topKFrequent()


"""
Runtime: 44 ms, faster than 71.88% of Python online submissions for Top K Frequent Words.
Memory Usage: 12.8 MB, less than 45.31% of Python online submissions for Top K
"""

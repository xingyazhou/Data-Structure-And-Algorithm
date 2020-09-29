# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 22:30:00 2020

Question
Given a list of timestamps in sequential order, return a list of lists grouped by week (7 days) using the first timestamp as the starting point.

Example:

ts = [
    '2019-01-01', 
    '2019-01-02',
    '2019-01-08', 
    '2019-02-01', 
    '2019-02-02',
    '2019-02-05',
]

output = [
    ['2019-01-01', '2019-01-02'], 
    ['2019-01-08'], 
    ['2019-02-01', '2019-02-02'],
    ['2019-02-05'],
]
 
@author: xingya
"""

from collections import defaultdict
from datetime import datetime

class Solution():
    def partitionTSByWeek(self, ts):
        if len(ts) == 0:
            return []
        
        d = defaultdict(list)
        
        for x in ts:
            w = self.string_to_week_number(x)
            d[w].append(x)
            
        return list(d.values())
            
    def string_to_week_number(self, string):
        return int(datetime.strptime(string, '%Y-%m-%d').strftime("%V"))
    

class Test():
    def testPartitionByWeek(self):
        ts = [
            '2019-01-01', 
            '2019-01-02',
            '2019-01-08', 
            '2019-02-01', 
            '2019-02-02',
            '2019-02-05',
            ]
        
        output = [
            ['2019-01-01', '2019-01-02'], 
            ['2019-01-08'], 
            ['2019-02-01', '2019-02-02'],
            ['2019-02-05'],
            ]
        
        s = Solution()
        
        partitioned = s.partitionTSByWeek(ts)
        
        assert partitioned == output
        print(partitioned)
        
        
t = Test()
t.testPartitionByWeek()
        
            
            




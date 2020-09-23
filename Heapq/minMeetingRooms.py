# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 20:33:50 2020

253. Meeting Rooms II (Medium)

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1

@author: xingya

"""


from heapq import heappush, heappop

class Solution:
    
    def minMeetingRooms(self, intervals):
        
        if len(intervals) == 0:
            return 0
        
        # ascendig order of meeting end time
        intervals.sort(key = lambda kv: kv[0])
        
        rooms = []    
        
        # push meeting end time to free_rooms
        heappush(rooms, intervals[0][-1])
        
        for i in intervals[1:]:
  
                # free_rooms[0] is the smallest element in heap
                if rooms[0] <= i[0]:
                    heappop(rooms)
                    
                heappush(rooms, i[-1])
        
        return len(rooms)
    
    
intervals = [[0, 30],[5, 10],[15, 20]]
s = Solution()
print(s.minMeetingRooms(intervals))

# Output
# 2

"""
Runtime: 56 ms, faster than 96.98% of Python online submissions for Meeting Rooms II.
Memory Usage: 15.9 MB, less than 91.99% of Python online submissions for Meeting
"""
        
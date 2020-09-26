# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 23:34:21 2020

973. K Closest Points to Origin (Medium)

We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
 

Note:

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000

@author: xingya
"""
import heapq

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        
        heap = []
        for x in points:
            heapq.heappush(heap, (x[0]**2 + x[1]**2, x))
        
        output = []
        for i in range(k):
            output.append(heapq.heappop(heap)[1])
        
        return output

points = [[3,3],[5,-1],[-2,4]]
k = 2            
s = Solution()
print(s.kClosest(points, k))     

"""
Runtime: 592 ms, faster than 87.37% of Python online submissions for K Closest Points to Origin.
Memory Usage: 19.6 MB, less than 15.85% of Python online submissions for K Closest Points to Origin.
"""
      
class Solution2(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """       
        points.sort(key = lambda x : x[0]**2+  x[1]**2)
        return points[:k]

points =[[1,3],[-2,2]]
k = 1           
s = Solution2()
print(s.kClosest(points, k))     

"""
Runtime: 528 ms, faster than 100.00% of Python online submissions for K Closest Points to Origin.
Memory Usage: 19.4 MB, less than 23.05% of Python online submissions for K Closest Points to Origin. 
""" 
        
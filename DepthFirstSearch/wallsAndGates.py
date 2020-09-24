# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 19:46:24 2020

286. Walls and Gates (Medium)


You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example: 

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4

@author: xingya

"""

INF =  2147483647
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """   
        if len(rooms)== 0:
            return []
        
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:  
                    self.dfs(rooms, i, j)

        return rooms
                   
    def dfs(self, rooms, i, j):
            
        r = len(rooms)
        c = len(rooms[0])           
        d = rooms[i][j] + 1

        if i-1 >= 0 and rooms[i-1][j] != -1 and rooms[i-1][j] > d:
            rooms[i-1][j] = d
            self.dfs(rooms, i-1, j)
       
        if i+1 < r and rooms[i+1][j] != -1 and rooms[i+1][j] > d:
            rooms[i+1][j] = d
            self.dfs(rooms, i+1, j)
                
        if j-1 >= 0 and rooms[i][j-1] != -1 and rooms[i][j-1] > d:
            rooms[i][j-1] = d
            self.dfs(rooms, i, j-1)
                
        if j+1 < c and rooms[i][j+1] != -1 and rooms[i][j+1] > d:
            rooms[i][j+1] = d
            self.dfs(rooms, i, j+1)
            
class Test(object):
    def test(self):
         
        rooms= [
                [INF,  -1 , 0 , INF],
                [INF, INF, INF,  -1],
                [INF,  -1, INF,  -1],
                [0,  -1, INF, INF],   
                ]  
        
        s = Solution()
        output = s.wallsAndGates(rooms)     
        expected = [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]
        
        assert (output == expected), "Wrong output, expcted output: [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]] "
        print(output)

t = Test()
t.test()

"""
Runtime: 228 ms, faster than 92.37% of Python online submissions for Walls and Gates.
Memory Usage: 19.7 MB, less than 23.47% of Python online submissions for Walls and
"""
        
    
        
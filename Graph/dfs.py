# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 12:46:30 2020

@author: xingya
"""

from collections import defaultdict

class Graph:
    def __init__(self, n):
        # numOfV: total number of vertice in graph
        self.numOfV = n
        self.graph = defaultdict(list)
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
        
    # Depth First Traversal, start from vertice v 
    def DFS(self, v): 
        
        output = []
        visited = [False] * self.numOfV
        
        for i in range(self.numOfV):                        
            if visited[i] == False:
                # vertice i is not visited before
                # recursive DFSUtil
                self.DFSUtil(visited, output,i)
                
        return (output)
        
        
    def DFSUtil(self, visited, output, i): 
        
        # i is visited now
        visited[i]= True      
        output.insert(0,i)

        for j in self.graph[i]: 
            if visited[j] == False: 
                # vertice j is not visited before
                # recursive DFSUtil
                self.DFSUtil(visited, output, j) 

   
# Test Graph    
g = Graph(5) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 4) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 4) 

print(g.DFS(0))

# Output [3, 2, 4, 1, 0]
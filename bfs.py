# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 19:40:12 2020

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
        
    def BFS(self, v):
        
        visited = [False ] * self.numOfV
        output = []
        
        # build a queue for BFS
        queue = []   
        queue.append(v)
        
        # set first node to True (visited) 
        # append first node to output list
        visited[v] = True
        
        # insert v to the left side of the list
        output.insert(0,v)
        
        while queue:
            # dequeue a node from queue when it is not empty
            # queue.pop(0) will pop element from the left side of the list (FIFO)
            u = queue.pop(0)
            
            # traverse all adjacent vertices of the vertice u
            for v in self.graph[u]:
                if visited[v] == False:
                    # vertice v has not been visited
                    # add vertice v to BFS queue
                    queue.append(v)
                    
                    # set node v as visited
                    visited[v] = True
                    
                    # apppend node v to output list
                    # insert v to the left side of the list
                    output.insert(0,v)
                    
        return output

# Test Graph    
g = Graph(5) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 4) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 4) 

print(g.BFS(0))

# Output [3, 4, 2, 1, 0]
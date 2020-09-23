# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 21:18:53 2020

Kruskal’s Minimum Spanning Tree Algorithm

 A minimum spanning tree (MST) or minimum weight spanning tree for a weighted, connected and undirected graph is a spanning tree with 
 weight less than or equal to the weight of every other spanning tree. The weight of a spanning tree is the sum of weights given to each edge of the spanning tree.
 
 A minimum spanning tree has (V – 1) edges where V is the number of vertices in the given graph.
 
Steps to find MST with Kruskal's Algorithm
1. Sort all the edges in non-decreasing order of their weight.
2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it.
    2.1 Use the Union-Find Algorithm to detect a cycle
3. Repeat step#2 until there are (V-1) edges in the spanning tree.

@author: xingya
"""

class Graph():
    def __init__(self, vertice):
        self.v = vertice
        self.graph = []
        
    def addEdge(self, u, v, w):
        self.graph.append([u,v,w])
        
    def findParent(self, parent, i):
        if parent[i] == i:
            return i
        else:
            return self.findParent(parent, parent[i]) 
    
    def union(self, parent, u, v):
        x = self.findParent(parent, u)
        y = self.findParent(parent, v)
        parent[x] = y
        
    def kruskal_mst(self):
        
        parent = []       
        for j in range(self.v):
            parent.append(j)
            
        self.graph.sort(key = lambda x:x[2])

        i = 0
        mst =[]
        numOfEdge = 0
        
        while numOfEdge < self.v - 1:
            
            u,v,w = self.graph[i]
            i += 1
            
            x = self.findParent(parent, u)
            y = self.findParent(parent, v)
            
            if x != y:
                # there will be no cycle formed when adding edge [u, v, w] to MST
                numOfEdge += 1
                mst.append([u,v,w])
                self.union(parent, u, v)

        return mst
                
                
g = Graph(4)
g.addEdge(0,1,10)
g.addEdge(0,2,6)
g.addEdge(0,3,5)
g.addEdge(1,3,15)
g.addEdge(2,3,4)

print(g.kruskal_mst())

# Output
# [[2, 3, 4], [0, 3, 5], [0, 1, 10]]
    
    


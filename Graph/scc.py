# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 23:04:22 2020

@author: xingy
"""

# DAG: Directed Acyclic Graph ( No cycles
# A digraph has atopoligical order if No directed cycle)

# Strongly-Connected Components
# vertices V and W are strongly connected, if there is a
# directred path from V to W and a directed path from W to V

# Kosaraju-Sharir algorithm:
# 1. Compute reverse postorder (topological order) in Reverse G
# 2. Run DFS in G, visited unmarked vertice in reverse postorder of Reverse G


from collections import defaultdict

count = -1

class Graph:
    
    def __init__(self, vertice):
        self.v = vertice
        self.graph = defaultdict(list)
        self.graph_R = defaultdict(list)
        
    def addEdge(self, u, v):
        # add edge to graph
        self.graph[u].append(v)
        # add edge to reverse graph
        self.graph_R[v].append(u)
        
    def topologysort(self):
        visited = [False] * self.v
        
        output=[]      
        for i in range(self.v):
            if visited[i] == False:
                self.dfs_RG(visited, output, i)
                
        return output

    def dfs_RG(self, visited, output, i):
        visited[i] = True
  
        for u in self.graph_R[i]:
            if visited[u] == False:
                self.dfs_RG(visited, output, u)
                
        output.insert(0,i)
        
        
    def is_scc(self):
        scc = [0] * self.v 
        visited = [False] * self.v
        global count
        
        topsort = self.topologysort()
        
        for i in topsort:
            if visited[i] == False:
                count += 1
                self.dfs_g(visited, scc, i)
                
        return scc
    
    
    def dfs_g(self, visited, scc, i):
        visited[i] = True
        scc[i] = count
        
        for u in self.graph[i]:
            if visited[u] == False:
                self.dfs_g(visited, scc, u)
        
                       
g= Graph(13)
g.addEdge(4,2)
g.addEdge(2,3)
g.addEdge(6,0)
g.addEdge(0,1)
g.addEdge(2,0)
g.addEdge(11,12)
g.addEdge(12,9)
g.addEdge(9,10)
g.addEdge(9,11)
g.addEdge(7,9)
g.addEdge(10,12)
g.addEdge(11,4)
g.addEdge(4,3)
g.addEdge(3,5)
g.addEdge(6,8)
g.addEdge(8,6)
g.addEdge(5,4)
g.addEdge(0,5)
g.addEdge(6,4)
g.addEdge(6,9)
g.addEdge(7,6)

print("topological order:")
print( g.topologysort() )

print("\nStrongly Connected Components:")
print( g.is_scc() )

# Output:
# topological order:
# [1, 0, 2, 4, 5, 3, 11, 9, 12, 10, 6, 7, 8]

# Strongly Connected Components:
# [1, 0, 1, 1, 1, 1, 3, 4, 3, 2, 2, 2, 2]

        
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 09:47:05 2020

@author: xingya
"""
from collections import defaultdict
import sys

class Heap():
    def __init__(self):
        self.size = 0
        self.pos = []
        self.array = []
        
    def heapsort(self):
        n = self.size
        
        for i in range(n):
            self.heapify(self.array, n, i)
            
    def heapify(self, a, n, i):
        l = i * 2 + 1
        r = i * 2 + 2
        
        smallest = i
        
        if l < n and a[l][1] < a[smallest][1]:
            smallest = l
            
        if r < n and a[r][1] < a[smallest][1]:
            smallest = r
            
        if i != smallest:
            u = a[smallest][0]
            v = a[i][0]
            
            a[i], a[smallest] = a[smallest], a[i]
            self.pos[u], self.pos[v] = self.pos[v], self.pos[u]

            self.heapify(a, n, smallest)
            
    def extractMin(self):
        minnode = self.array[0]    
        u = self.array[0][0]
        v = self.array[self.size-1][0]
        
        self.pos[u], self.pos[v] = self.pos[v], self.pos[u]
        
        self.array[0], self.array[self.size - 1] = self.array[self.size - 1], self.array[0]
        self.size -= 1
        return minnode
    
class Graph():
    def __init__(self, vertice):
        self.v = vertice
        self.graph = defaultdict(list)
        
    def addEdge(self, u, v, w):
        self.graph[u].append([v, w])
        self.graph[v].append([u, w])
        
    def primMST(self):
        h = Heap()
        num = self.v
        parent = [-1]*num
        
        for node in range(self.v):
            h.array.append([node, sys.maxsize])  
            h.pos.append(node)
            
        h.size = self.v
        
        h.array[0][1] = 0
        parent[0] = 0
        
        while h.size > 0:
            minnode = h.extractMin()
            
            h.heapsort()
            u = minnode[0]
            
            for neigh in self.graph[u]:
                v, w = neigh[0], neigh[1]
                posheap = h.pos[v]
                
                if posheap < h.size and w < h.array[posheap][1]:
                    h.array[posheap][1] = w
                    
                    parent[v] = u
                    
            h.heapsort()
            
        return h.array
        

g = Graph(9)
g.addEdge(0,1,4)
g.addEdge(0,7,8)
g.addEdge(1,2,8)
g.addEdge(1,7,11)
g.addEdge(2,3,7)
g.addEdge(2,8,2)
g.addEdge(2,5,4)
g.addEdge(3,4,9)
g.addEdge(3,5,14)
g.addEdge(4,5,10)
g.addEdge(5,6,2)
g.addEdge(6,7,1)
g.addEdge(6,8,6)
g.addEdge(7,8,7)

print(g.primMST())

# Output
# [[4, 9], [3, 7], [8, 2], [2, 4], [5, 2], [6, 1], [7, 8], [1, 4], [0, 0]]
        
        
        
        
        
        
        
        
        
        
 

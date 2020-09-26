# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 09:47:05 2020

[Definition of MST From Wikipedia]
A minimum spanning tree (MST) or minimum weight spanning tree is a subset of the edges of a connected, edge-weighted undirected graph 
that connects all the vertices together, without any cycles and with the minimum possible total edge weight. That is, it is a spanning 
tree whose sum of edge weights is as small as possible. More generally, any edge-weighted undirected graph (not necessarily connected) 
has a minimum spanning forest, which is a union of the minimum spanning trees for its connected components.

@author: xingya
"""



from collections import defaultdict
import sys

class Heap():
    
## Min Heaps are binary trees for which every parent node has a value less than or equal to any of its children. 
## This implementation uses arrays for which heap[k] <= heap[2*k+1] and heap[k] <= heap[2*k+2] for all k, 
## counting elements from zero. 
## heap[0] is always the smallest item

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
            # self.pos is used to record the position of a node in the Heap 
            self.pos[u], self.pos[v] = self.pos[v], self.pos[u]

            self.heapify(a, n, smallest)
            
    def extractMin(self):
        minnode = self.array[0] 
        
        # root node
        u = self.array[0][0]
        # last node
        v = self.array[self.size-1][0]
        
        # swap root node with last node
        self.pos[u], self.pos[v] = self.pos[v], self.pos[u]      
        self.array[0], self.array[self.size - 1] = self.array[self.size - 1], self.array[0]
        
        # reduce heap size
        self.size -= 1
        # heapify root
        self.heapify(self.array, self.size, 0)
        
        return minnode
    
    def put(self, i, w):
        
        self.array[i][1] = w
        self.heapsort()
    
class Graph():
    def __init__(self, vertice):
        self.v = vertice
        self.graph = defaultdict(list)
        
    def addEdge(self, u, v, w):
        self.graph[u].append([v, w])
        self.graph[v].append([u, w])
    
    def printArr(self, parent, n): 
        for i in range(1, n): 
            print ("% d - % d" % (parent[i], i) )
            
    def primMST(self):

        num = self.v
        parent = [-1]*num
        
        h = Heap()
        h.size = self.v
        for node in range(self.v):
            h.array.append([node, sys.maxsize])  
            h.pos.append(node)
            
        h.array[0][1] = 0
        parent[0] = 0
        
        while h.size > 0:
            
            minnode = h.extractMin()
            u = minnode[0]

            for neigh in self.graph[u]:
                
                v, w = neigh[0], neigh[1]
                posheap = h.pos[v]
                
                if posheap < h.size and w < h.array[posheap][1]:
                    h.put(posheap, w)
                    parent[v] = u
                    
        self.printArr(parent, self.v )  
        
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
# 0 -  1
# 1 -  2
# 2 -  3
# 3 -  4
# 2 -  5
# 5 -  6
# 6 -  7
# 2 -  8
# [[4, 9], [3, 7], [7, 1], [6, 2], [5, 4], [8, 2], [2, 8], [1, 4], [0, 0]]
        


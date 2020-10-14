# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 14:16:55 2020

208. Implement Trie (Prefix Tree) (Medium)

Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.

@author: xingya
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        cur_node = self.root
        
        for char in word:
            if char not in cur_node.children:
                cur_node.children[char] = TrieNode()
                
            cur_node = cur_node.children[char]
            
        cur_node.isEnd = True
        
        return self.root
    
    def search(self, word):
        cur = self.root
        
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        
        return cur.isEnd
    
    def startsWith(self, word):
        cur = self.root
        
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
            
        return True
        

class Test:
    def testTrie(self):
        
        t = Trie()
        
        t.insert('apple')      
        output1 = t.search('apple')     # True
        output2 = t.search('app')       # False
        output3 = t.startsWith('app')   # True
        t.insert('app')
        output4 = t.search('app')       # True
        
        print(output1, output2, output3, output4)
        
        assert output1 == True
        assert output2 == False
        assert output3 == True
        assert output4 == True
        
t = Test()
t.testTrie()        
            
        

"""
Runtime: 164 ms, faster than 79.79% of Python3 online submissions for Implement Trie (Prefix Tree).
Memory Usage: 31.3 MB, less than 5.95% of Python3 online submissions for Implement Trie (Prefix Tree).
"""


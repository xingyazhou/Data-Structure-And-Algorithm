# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 12:23:31 2020

Design Linked List
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
 

Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3
 

Constraints:

0 <= index, val <= 1000
Please do not use the built-in LinkedList library.
At most 2000 calls will be made to get, addAtHead, addAtTail,  addAtIndex and deleteAtIndex.

@author: xingya

"""

class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.linkedlist = None 
        
    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1
        
        cur = self.linkedlist
        for i in range(index):
            cur = cur.next        
        return cur.val
                     
    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        if self.linkedlist is None:
            self.linkedlist = ListNode(val)
            
        else:
            prev = self.linkedlist
            self.linkedlist = ListNode(val)
            self.linkedlist.next = prev
        self.size += 1

        return self.linkedlist
      
    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        if self.linkedlist is None:
            self.linkedlist = ListNode(val)
            
        else:
            prev = self.linkedlist
            for _ in range(self.size-1):
                prev = prev.next
            prev.next = ListNode(val)
                
        self.size += 1
        return self.linkedlist
        
    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0 or index > self.size:
            return 
        
        if index == 0:
            self.addAtHead(val)
            return 
        
        pred = self.linkedlist
        for _ in range(index-1):
            pred = pred.next
            
        to_add = ListNode(val)
        to_add.next = pred.next
        pred.next = to_add
        self.size += 1
             
        return self.linkedlist
        
    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """      
        if index < 0 or index >= self.size:
            return

        if self.size == 1:
            self.linkedlist = None
            return None
        
        if index == 0:
            self.linkedlist = self.linkedlist.next
            self.size -= 1
            return None
          
        prev = self.linkedlist
        for _ in range(index-1 ):
            prev = prev.next
        
        if index == self.size - 1:
            prev.next = None
            self.size -= 1
        else:
            prev.next = prev.next.next
            self.size -= 1
        
                
obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(3)
l=obj.addAtIndex(1, 2)
print( obj.get(1))
obj.deleteAtIndex(1)
print( obj.get(1))

# Output
# 2
# 3

"""
Runtime: 216 ms, faster than 75.40% of Python online submissions for Design Linked List.
Memory Usage: 13.5 MB, less than 43.57% of Python online submissions for Design Linked List.
"""

        
        


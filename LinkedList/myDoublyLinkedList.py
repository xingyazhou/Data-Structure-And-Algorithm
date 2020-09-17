# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 14:38:22 2020

@author: xingy
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 12:23:31 2020

707. Design Linked List (Medium)

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
        self.prev = None

class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.head = ListNode(0)
        self.tail = ListNode(0)
        
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1
        
        cur = self.head.next
        for i in range(index):
            cur = cur.next        
        return cur.val
                     
    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        to_add = ListNode(val)
        to_add.next = self.head.next
        to_add.prev = self.head
               
        self.head.next.prev = to_add
        self.head.next = to_add
        self.size += 1
        
    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        to_add = ListNode(val)
        to_add.prev = self.tail.prev
        to_add.next = self.tail
        
        self.tail.prev.next = to_add
        self.tail.prev = to_add
        
        #print(val,self.tail.val, self.tail.prev.val )
        #print(self.head.next.val)
        self.size += 1
        
        return self.head
                
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
        
        pred = self.head
        for _ in range(index):
            pred = pred.next
            
        succ = pred.next
            
        to_add = ListNode(val)
        to_add.next = succ
        to_add.prev = pred
        
        pred.next = to_add
        succ.prev = to_add
        self.size += 1
             
        return self.head
        
    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """      
        if index < 0 or index >= self.size:
            return
          
        prev = self.head
        
        for _ in range(index ):
            prev = prev.next
        
        succ = prev.next.next       
        prev.next = succ
        succ.prev = prev
        
        self.size -= 1
             
obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1, 2)
print( obj.get(1))
obj.deleteAtIndex(1)
print(obj.get(1))


# Output
# 2
# 3


"""
Runtime: 140 ms, faster than 88.71% of Python online submissions for Design Linked List.
Memory Usage: 15.1 MB, less than 6.77% of Python online submissions for Design Linked List.
"""

        
        


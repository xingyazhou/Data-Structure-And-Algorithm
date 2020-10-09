# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 12:09:59 2020

19. Remove Nth Node From End of List (Medium)

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

@author: xingy
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
class Solution:
    def removeNthFromEnd(self, head, n):
        if head is None:
            return head
        
        length = 0
        cur = head
        
        while cur is not None:
            length += 1
            cur = cur.next
            
        cur = head
        prev = head
        key = length - n + 1
        
        if n == 1 and length == 1:
            return None
            
        if key == 1 and length > 1:
            return head.next
        
        count = 0
        while cur is not None:
            count += 1
            
            if count == key:
                prev.next = cur.next
                cur = cur.next

            else:
                prev = cur
                cur = cur.next
                
        return head
    

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
n = 2

s = Solution()
output = s.removeNthFromEnd(head, n)

while output is not None:
    print(output.val)
    output = output.next
    
    

# Output
# 1
# 2
# 3
# 5


"""
Runtime: 28 ms, faster than 91.64% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 14 MB, less than 99.98% of Python3 online submissions for Remove Nth Node From End of List.
"""
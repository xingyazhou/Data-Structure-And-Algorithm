# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 22:09:07 2020

2. Add Two Numbers (Medium)
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

@author: xingya

"""

class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        head = ListNode(0)
        prev = head        
        flag = 0
        
        while l1 and l2:
            m = l1.val + l2.val + flag
            
            if m < 10:
                flag = 0       
            else:
                flag = 1
                
            prev.next = ListNode(m % 10)          
            prev = prev.next
              
            l1 = l1.next
            l2 = l2.next
            
        while l1:
            m = l1.val + flag
            
            if m < 10:
                flag = 0
            else:
                flag = 1
                
            prev.next = ListNode(m % 10)
            prev = prev.next               
            l1 = l1.next

        while l2:
            m = l2.val + flag
            if m < 10:
                flag = 0
            else:
                flag = 1
                
            prev.next = ListNode(m % 10)
            prev = prev.next
            
            l2 = l2.next

            
        if flag == 1:
            prev.next = ListNode(1)
            
        return head.next
        
l1 = ListNode(2)           
l1.next = ListNode(4) 
l1.next.next = ListNode(3)

l2 = ListNode(5)           
l2.next = ListNode(6) 
l2.next.next = ListNode(4)

s = Solution()
h = s.addTwoNumbers(l1, l2)

while h:
    print(h.val)
    h = h.next
    
# Output
# 7
# 0
# 8
    
    
    
"""
Runtime: 52 ms, faster than 96.19% of Python online submissions for Add Two Numbers.
Memory Usage: 12.6 MB, less than 93.13% of Python online submissions for Add Two Numbers.
"""



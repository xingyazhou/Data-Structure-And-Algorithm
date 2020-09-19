# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 20:42:46 2020

21. Merge Two Sorted Lists (Easy)
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
@author: xingya
"""

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2) :
             
        if l1 is None:
            return l2
        
        if l2 is None:
            return l1
        
        if l1.val < l2.val:
            head = l1
            l1=l1.next
            
        else:
            head = l2
            l2=l2.next
        
        m = head
            
        while l1 and l2:
            if l1.val < l2.val:
                m.next = l1             
                l1 = l1.next
                
            else:
                m.next = l2     
                l2 = l2.next
                
            m = m.next
        
        if l1:
            m.next = l1
            
        if l2:
            m.next = l2
            
        return head
  
    
# Time complexity : O(n + m)
# Space complexity : O(1)

    
"""   
Runtime: 24 ms, faster than 99.76% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 14 MB, less than 20.66% of Python3 online submissions for Merge Two Sorted Lists.
"""
            
    
        
        
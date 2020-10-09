# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 10:51:20 2020

83. Remove Duplicates from Sorted List (Easy)

Share
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3

@author: xingya
"""

#Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def deleteDuplicates(self, head) :
        if head is None:
            return head
        
        first = head
        second = head.next
        
        while second is not None:
            if second.val == first.val:
                first.next = second.next
                second = first.next
            else:
                first = first.next
                second = second.next

        return head
    
    
                
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)

s = Solution()
l = s.deleteDuplicates(head)

while (l):
    print(l.val)
    l = l.next


"""
Runtime: 36 ms, faster than 95.03% of Python3 online submissions for Remove Duplicates from Sorted List.
Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Remove Duplicates from Sorted List.
"""




        
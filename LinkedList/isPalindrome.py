# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 20:18:32 2020

234. Palindrome Linked List (Easy)
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?

@author: xingya
"""

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        if head is None or head.next is None:
            return True
        
        curr = head
        l=[]
        r=[]

        while curr:
            l.append(curr.val)
            curr = curr.next

        r=l[::-1]
        
        if r==l:
            return True
    
        return False
            
"""
Runtime: 68 ms, faster than 88.50% of Python3 online submissions for Palindrome Linked List.
Memory Usage: 23.9 MB, less than 80.73% of Python3 online submissions for Palindrome Linked List.
"""
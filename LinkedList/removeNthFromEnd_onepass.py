# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 13:09:00 2020

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
 
@author: xingya
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
        
        dumy = ListNode(0)
        dumy.next = head
        first = dumy
        second = dumy
        
        count = 1
        while count <= n+1:
            
            first = first.next
            count += 1
        
        while first is not None:
            first = first.next
            second = second.next
               
        second.next = second.next.next
        
        return dumy.next
           
class Test():
    def testremoveNthFromEnd(self):
        head1 =ListNode(1)
        head1.next = ListNode(2)
        head1.next.next = ListNode(3)
        head1.next.next.next = ListNode(4)
        head1.next.next.next.next = ListNode(5)
        n1 = 2
        
        head2 = ListNode(1)
        n2 = 1
        
        expected1 = [1,2,3,5]
        expected2 = []
        
        s = Solution()
        r1 = s.removeNthFromEnd(head1, n1)
        r2 = s.removeNthFromEnd(head2, n2)
        
        output1 = []
        output2 = []
        
        while r1 is not None:
            output1.append(r1.val)
            r1 = r1.next
            
        while r2 is not None:
            output2.append(r2)
            r2 = r2.next
            
        print(output1, output2)
        
        assert output1 == expected1, "wrong result, expected output is: [1,2,3,5]"
        assert output2 == expected2, "Wrong result, expected output is []"
        
     
t = Test()
t.testremoveNthFromEnd()     

# Output
# [1, 2, 3, 5] []
        

"""    
Runtime: 28 ms, faster than 91.64% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 14 MB, less than 99.98% of Python3 online submissions for Remove Nth Node From End of List.
"""
    


# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 13:47:32 2020

82. Remove Duplicates from Sorted List II (Medium)
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Return the linked list sorted as well.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3

@author: xingya

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def deleteDuplicates(self, head):
        
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        cur = head
        
        count = 1
        while cur is not None:
            if cur.next is None:
                if count > 1:
                    prev.next = cur.next
                return dummy.next
            
            else:
                if cur.val != cur.next.val:
                    if count > 1:
                        prev.next = cur.next
                        cur = cur.next
                        count = 1
                    
                    else:
                        prev = prev.next
                        cur = cur.next
                elif cur.val == cur.next.val:
                    count += 1
                    cur = cur.next
                    
        return dummy.next
    
    
class Test:
    def testDeleteDuplicates(self):
        
        # Create a Linked-list
        head1 = ListNode(1)
        l = [5, 4, 4, 3, 3, 2]
        cur = head1
        while l:
            cur.next = ListNode(l.pop())
            cur = cur.next
        
        # Create a Linked-list
        head2 = ListNode(1)
        head2.next = ListNode(1)
        head2.next.next = ListNode(1)
        head2.next.next.next = ListNode(2)
        head2.next.next.next.next = ListNode(3)
        
        expected1 = [1,2,5]
        expected2 = [2,3]
        
        s = Solution()
        r1 = s.deleteDuplicates(head1)
        r2 = s.deleteDuplicates(head2)
        
        output1=[]
        output2=[]
        
        cur1 = r1
        while cur1 is not None:
            output1.append(cur1.val)
            cur1 = cur1.next
        
        cur2 = r2
        while cur2 is not None:
            output2.append(cur2.val)
            cur2 = cur2.next
            
        print(output1, output2)
        
        assert output1 == expected1, "Wrong result, expected output is : [1,2,5]"
        assert output2 == expected2, "Wrong result, expected output is : [2,3]"
        
t = Test()
t.testDeleteDuplicates()

"""
Runtime: 36 ms, faster than 92.99% of Python3 online submissions for Remove Duplicates from Sorted List II.
Memory Usage: 14.2 MB, less than 99.93% of Python3 online submissions for Remove Duplicates from Sorted List II.
"""
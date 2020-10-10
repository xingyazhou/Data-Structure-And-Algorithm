# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 14:39:41 2020

86. Partition List (Medium)
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5

@author: xingya
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        
        dummys = ListNode(0)
        curs = dummys
        
        dummyb = ListNode(0)
        curb = dummyb
        
        
        cur = head      
        while cur:
            if cur.val < x:
                curs.next = cur
                curs = cur
                
            else:
                curb.next = cur
                curb = cur
                
            cur = cur.next
                
        curb.next = None
        curs.next = dummyb.next
        
        return dummys.next
    
class Test:
    def testPartition(self):
        
        # Create a Linked-list
        head = ListNode(1)
        l = [2, 5, 2, 3, 4]
        cur = head
        while l:
            cur.next = ListNode(l.pop())
            cur = cur.next
            
        x = 3
        
        expected = [1,2,2,4,3,5]
        
        s = Solution()
        r = s.partition(head, x)
        
        output = []
        while r:
            output.append(r.val)
            r = r.next
            
        print(output)      
        assert output == expected, "Wrong result, expected output is: [1, 2, 2, 4, 3, 5]"

t = Test()
t.testPartition()            
        

"""
Runtime: 28 ms, faster than 95.54% of Python3 online submissions for Partition List.
Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Partition List.
"""


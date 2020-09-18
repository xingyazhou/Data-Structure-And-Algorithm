# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 09:30:24 2020

141. Linked List Cycle (Easy)
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Follow up:
Can you solve it using O(1) (i.e. constant) memory?

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 
Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.

@author: xingya

"""

class ListNode():
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def hasCycle(self, head):
        if head is None:
            return False
        
        
        p1 = head
        p2 = head
        
        while p1 and p2:
            p1 = p1.next
            if p2.next is not None:
                if p2.next.next is not None:
                    p2=p2.next.next
                else:
                    return False
            else:
                return False
            
            if p1 == p2:
                return True
        return False
        


head1 = ListNode(3)
prev = head1
prev.next = ListNode(2)
succ = prev.next
prev = prev.next
prev.next = ListNode(0)
prev = prev.next
prev.next = ListNode(-4)
prev=prev.next
prev.next = succ

head2 = ListNode(3)
prev = head2
prev.next = ListNode(2)
prev = prev.next
prev.next = ListNode(0)
prev = prev.next
prev.next = ListNode(-4)

s = Solution()
print(s.hasCycle(head1))
print(s.hasCycle(head2))
    
# Output
# True
# False

# Time complexity : O(n)
# Space complexity : O(1)

"""  
Runtime: 44 ms, faster than 92.21% of Python3 online submissions for Linked List Cycle.
Memory Usage: 16.8 MB, less than 80.43% of Python3 online submissions for Linked List Cycle.
"""

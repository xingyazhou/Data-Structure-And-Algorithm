# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 09:59:56 2020

142. Linked List Cycle II (Medium)
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Notice that you should not modify the linked list.

Follow up:

Can you solve it using O(1) (i.e. constant) memory?

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
Example 2:


Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
Example 3:

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.

@author: xingya

Remaining Question:
Can you solve it using O(1) (i.e. constant) memory?
    
"""

# Definition for singly-linked list.
class ListNode():
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
       
    def detectCycle(self, head) :
        if head is None:
            return
        
        node = head
        visited = set()
                       
        while node:
            if node in visited:
                return node
            
            else:
                visited.add(node)
                node = node.next
           
        return 
        
        
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


s = Solution()
print(s.detectCycle(head1).val)

# Time complexity : O(n)
# Space complexity : O(n)

"""
Runtime: 44 ms, faster than 96.61% of Python3 online submissions for Linked List Cycle II.
Memory Usage: 17.2 MB, less than 11.03% of Python3 online submissions for Linked List Cycle II.
"""
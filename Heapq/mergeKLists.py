# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 13:10:43 2020

23. Merge k Sorted Lists (Hard)
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []

Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.

@author: xingya
"""

from heapq import heappush, heappop

class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return
        
        h = []     
        for l in lists:           
            while l:
                heappush(h, l.val)
                l = l.next
       
        head = ListNode(0)
        mergedList = head
        
        while h:
            x=heappop(h)
            mergedList.next = ListNode(x)
            mergedList = mergedList.next
 
        return head.next
                

    def test(self):
        
        list1 = ListNode(1)        
        list1.next = ListNode(4)
        list1.next.next = ListNode(5)
        
        list2 = ListNode(1)        
        list2.next = ListNode(3)
        list2.next.next = ListNode(4)
        
        list3 = ListNode(2)
        list3.next = ListNode(6)
        
        lists=[]
        lists.append(list1)
        lists.append(list2)
        lists.append(list3)

        s=Solution()
        outputList = s.mergeKLists(lists)
        
        mergedList = []
        while outputList:
            mergedList.append(outputList.val)
            outputList = outputList.next

        expectedList = [1, 1, 2, 3, 4, 4, 5, 6]
        assert (mergedList == expectedList), "wrong result, expected output is [1, 1, 2, 3, 4, 4, 5, 6]"
        print(mergedList)

s = Solution()
s.test()   

# Output
# [1, 1, 2, 3, 4, 4, 5, 6]


"""
Runtime: 108 ms, faster than 66.89% of Python online submissions for Merge k Sorted Lists.
Memory Usage: 21.5 MB, less than 39.76% of Python online submissions for Merge k
"""






        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
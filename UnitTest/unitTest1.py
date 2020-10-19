# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 22:37:00 2020

@author: xingya
"""
import unittest
import pathsum
import diameterOfBinaryTree
import partition
import subarraySum

class Test(unittest.TestCase):
    
    def testDiameterOfBinayTree(self):
        print("\nStart Testing diameterOfBinaryTree ...")
        # Buid a Tree
        root = diameterOfBinaryTree.TreeNode(1)
        root.left = diameterOfBinaryTree.TreeNode(2)
        root.right = diameterOfBinaryTree.TreeNode(3)
        root.left.left = diameterOfBinaryTree.TreeNode(4)
        root.left.right = diameterOfBinaryTree.TreeNode(5)
        
        expected_pathlen = 3

        s = diameterOfBinaryTree.Solution()
        # Calculate the longest length of the path
        pathlen = s.diameterOfBinaryTree(root)
        
        print("The longest path: ", pathlen)
        self.assertEqual( pathlen , expected_pathlen)
        
    def testPathSum(self):
        print("\nStart Testing pathsum ...")
        # Build a tree     
        root = pathsum.TreeNode(10)
        root.left = pathsum.TreeNode(5)
        root.right = pathsum.TreeNode(-3)
        
        root.left.left = pathsum.TreeNode(3)
        root.left.right = pathsum.TreeNode(2)
        root.right.right = pathsum.TreeNode(11)
        
        root.left.left.left = pathsum.TreeNode(3)
        root.left.left.right = pathsum.TreeNode(-2)
        root.left.right.right = pathsum.TreeNode(1)
        
        expect = 3
    
        s = pathsum.Solution()
        output = s.pathSum(root, 8)
        
        print("The paths that sum to 8 are: ", output)
        assert output == expect
        
    def testPartition(self):
        print("\nStart Testing partition ...")
        # Create a Linked-list
        head = partition.ListNode(1)
        l = [2, 5, 2, 3, 4]
        cur = head
        while l:
            cur.next = partition.ListNode(l.pop())
            cur = cur.next
            
        x = 3  
        expected = [1,2,2,4,3,5]
        
        s = partition.Solution()
        r = s.partition(head, x)
        
        output = []
        while r:
            output.append(r.val)
            r = r.next
            
        print("New Partition: [1, 2, 2, 4, 3, 5]", output)      
        assert output == expected, "Wrong result, expected output is: [1, 2, 2, 4, 3, 5]"
        
    def testSubarraySum(self):

        print("\nStart Testing subarraySum ...")

        nums1 = [3,4,7,2,-3,1,4,2]
        k1 = 7
        expected1 = 4
        
        s = subarraySum.Solution()
        output1 = s.subarraySum(nums, k1)
        
        print("SubTest Case 1: nums = ", nums1, ", k = ", k1)
        print("The total number of continuous subarrays: ", output1)
        assert output1 == expected1
        
        nums2 = [1,1,1]
        k2=2
        expected2 = 2
        output2 = s.subarraySum(nums2, k2)
        print("\nSubTest Case 2: nums = ", nums2, ", k = ", k2)
        print("The total number of continuous subarrays: ", output2)
        assert output2 == expected2
        

 
if __name__ == '__main__':
    unittest.main()


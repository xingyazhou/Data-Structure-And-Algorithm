# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 23:45:20 2020

733. Flood Fill (Easy)

An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).
Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].

@author: xingya

"""

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        orgColor = image[sr][sc]
        if newColor != orgColor:
            self.dfs(image, sr, sc, newColor, orgColor)
        
        return image    
    
       
    def dfs(self, image, sr, sc, newColor, orgColor):
        
        image[sr][sc] = newColor
        
        nr = len(image)
        nc = len(image[0])
      
        
        if sr-1 >= 0 and image[sr-1][sc] == orgColor:
            self.dfs(image, sr-1, sc, newColor, orgColor)
              
        if sr+1 < nr and image[sr+1][sc] == orgColor:
            self.dfs(image, sr+1, sc, newColor, orgColor)
            
        if sc-1 >= 0 and image[sr][sc-1] == orgColor:
            self.dfs(image, sr, sc-1, newColor, orgColor)
            
        if sc+1 < nc and image[sr][sc+1] == orgColor:
            self.dfs(image, sr, sc+1, newColor, orgColor)
            


image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2      
s = Solution()
new_image = s.floodFill(image, sr,sc,newColor)

def assert_check(new_image):
    assert (new_image == [[2, 2, 2], [2, 2, 0], [2, 0, 1]] ), "Wrong image, Expected [[2, 2, 2], [2, 2, 0], [2, 0, 1]]!"
    print(new_image)

assert_check(new_image)

# output
# [[2, 2, 2], [2, 2, 0], [2, 0, 1]]

"""
Runtime: 60 ms, faster than 86.71% of Python online submissions for Flood Fill.
Memory Usage: 12.7 MB, less than 93.61% of Python online submissions for Flood Fill.
"""


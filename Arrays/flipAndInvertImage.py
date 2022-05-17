# 832. Flipping an Image EASYY

# Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.

# To flip an image horizontally means that each row of the image is reversed.

# For example, flipping [1,1,0] horizontally results in [0,1,1].
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.

# For example, inverting [0,1,1] results in [1,0,0].
 

# Example 1:

# Input: image = [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]
# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
# Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
  
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        rev_out = []
        for row in image:
            inner_row = [row[i] for i in reversed(range(len(row)))] # Can also use inner_row = row[::-1] but its slower
            inverted_row = []
            for val in inner_row:
                inverted_row.append(val^1)
            rev_out.append(inverted_row)
        return(rev_out)

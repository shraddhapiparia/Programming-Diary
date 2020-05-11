# 733. Flood Fill

#  An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

# Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

# To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

# At the end, return the modified image. 

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        todo, row, col, seen = [[sr,sc]], len(image), len(image[0]), []
        c = image[sr][sc]
        while todo:
            for v in todo:
                [i,j] = v
                seen.append([i,j])
                image[i][j] = newColor
                todo.append([i+1,j]) if i+1 < row and [i+1,j] not in seen and image[i+1][j] == c else None
                todo.append([i-1,j]) if i-1 >= 0 and [i-1,j] not in seen and image[i-1][j] == c else None  
                todo.append([i,j+1]) if j+1 < col and [i,j+1] not in seen and image[i][j+1] == c else None
                todo.append([i,j-1]) if j-1 >= 0 and [i,j-1] not in seen and image[i][j-1] == c else None
                todo.remove(v)
        return image 

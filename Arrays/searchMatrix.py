# 74. Search a 2D Matrix
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        left, right = 0, m*n-1
        
        while left <= right:
            pivot = (left+right)//2
            if target == matrix[pivot//n][pivot%n]:
                return True
            else:
                if target < matrix[pivot//n][pivot%n]:
                    right = pivot - 1
                else:
                    left = pivot + 1
        return False
        

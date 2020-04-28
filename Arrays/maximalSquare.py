class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        dp, M = [[0 for col in range(len(matrix[0])+1)] for row in range(len(matrix)+1)], 0
        
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if matrix[i-1][j-1] == "1":
                    l = [dp[i-1][j-1], dp[i][j-1], dp[i-1][j]]
                    dp[i][j] = min(l) + 1
                M = dp[i][j] if dp[i][j] > M else M
                
        return M * M
        
# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
# Input: 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# Output: 4

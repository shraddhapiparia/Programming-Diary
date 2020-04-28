class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        l,maxlen = len(matrix[0]), 0
        dp = [[0]* l+1 for _ in range(l+1)]
        for i in range(1,l):
            for j in range(1,l):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
                    maxlen = dp[i][j] if dp[i][j] > maxlen else maxlen
        return maxlen * maxlen
        
# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
# Input: 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# Output: 4

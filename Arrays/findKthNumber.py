# 668. Kth Smallest Number in Multiplication Table
# Nearly everyone has used the Multiplication Table. The multiplication table of size m x n is an integer matrix mat where mat[i][j] == i * j (1-indexed).

# Given three integers m, n, and k, return the kth smallest element in the m x n multiplication table.

# Example 1:
# Input: m = 3, n = 3, k = 5
# Output: 3
# Explanation: The 5th smallest number is 3.

# Example 2:
# Input: m = 2, n = 3, k = 6
# Output: 6
# Explanation: The 6th smallest number is 6.
 
# Constraints:
# 1 <= m, n <= 3 * 104
# 1 <= k <= m * n

class Solution:
    def kSmallerValues(self, m, n, k, mid):
        j, count = n, 0
        for i in range(1,m+1):
            while j >= 1 and i*j > mid:
                j -= 1
            count += j
        if count < k:
            return False
        else:
            return True
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        lo, hi = 1, m*n
        while lo <= hi:
            mid = lo + (hi-lo)//2
            if self.kSmallerValues(m, n, k, mid):
                hi = mid-1
            else:
                lo = mid+1
        return lo
            
        

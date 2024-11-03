# 70. Climbing Stairs 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# Fibonacci kind of sum
class Solution:
    def climbStairs(self, n: int) -> int:
        f_1 = 1
        f_2 = 2
        if n == 0:
            return None
        if n == 1:
            return f_1
        if n == 2:
            return f_2
        for i in range(2,n):
            f_c = f_1 + f_2
            f_1, f_2 = f_2, f_c
        return f_c
        
# More oprimized from above
class Solution:
    def climbStairs(self, n: int) -> int:
        f_1 = f_2 = 1
        if n == 0 or n == 1:
            return 1
        for i in range(2,n+1):
            f_1, f_2 = f_2, f_1+f_2
        return f_2
        
# Can use DP but it is not space optiized since we only need last two elements from DP
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1

        dp = [0] * (n+1)
        dp[0] = dp[1] = 1
        
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

# Use recursion
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)

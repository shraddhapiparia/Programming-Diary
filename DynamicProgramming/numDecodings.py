# 91. Decode ways
# A message containing letters from A-Z is being encoded to numbers using the following mapping:

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26

# Given a non-empty string containing only digits, determine the total number of ways to decode it.

# The answer is guaranteed to fit in a 32-bit integer.

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1
        for i in range(2, len(dp)):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            two_digit = int(s[i-2 : i])
            if two_digit >= 10 and two_digit <= 26:
                dp[i] += dp[i-2]
        return dp[len(s)]
        

# 1446. Consecutive Characters
# Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character. Return the power of the string.
# Input: s = "leetcode"
# Output: 2
# Explanation: The substring "ee" is of length 2 with the character 'e' only.

class Solution:
    def maxPower(self, s: str) -> int:
        if not s:
            return 0
        maxval = float('-inf')
        i = 0
        while i < len(s):
            j = i
            while i < len(s)-1 and s[i] == s[i+1]:
                i += 1
            if  len(s[j:i+1]) > maxval:
                maxval = len(s[j:i+1])
            i += 1
        return maxval 


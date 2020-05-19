# 567. Permutation in String

# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the 
# first string's permutations is the substring of the second string.

# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        plen, slen, out, y = len(s1), len(s2), [], {}
        for j in s1:
            y[j] = 1 if j not in y else y[j] + 1
        for i in range(slen-plen+1):
            x = {}
            for c in s2[i:plen+i]:
                x[c] = 1 if c not in x else x[c] + 1
            if x == y:
                return True

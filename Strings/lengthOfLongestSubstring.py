# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Basic solution with all possible cobinations
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sidx, curr, res = 0, 0, 0
        seen = set()
        while curr<len(s):
            if s[curr] not in seen:
                seen.add(s[curr])
            else:
                if len(seen) > res:
                    res = len(seen)
                seen = set()
                curr = sidx
                sidx += 1
            curr += 1
        return max(len(seen), res)

  # Improved version using sliding window
  class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, res = 0, 0
        seen = set()
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            res = max(res, right-left+1)
        return res

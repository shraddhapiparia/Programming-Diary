# 1528. Shuffle String EASY

# You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

# Return the shuffled string.

 

# Example 1:

# Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
# Output: "leetcode"
# Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.

# Simple solution
class Solution:
    def restoreString(self, s, indices):
        ans = [None] * len(s)
        for i,c in enumerate(s): ans[indices[i]] = c
        return "".join(ans)
      
# One liner
class Solution:
    def restoreString(self, s, indices):
        return "".join([c for i,c in sorted(zip(indices,s))])
      
# Restructure array index
class Solution:
    def restoreString(self, s, indices):
        arr = [None] * len(s)
        for i,v in enumerate(indices): arr[v] = i
        return "".join([s[arr[i]] for i in range(len(s))])

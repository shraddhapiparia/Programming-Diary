# 266. Palindrome Permutation
# Given a string s, return true if a permutation of the string could form a 
# palindrome and false otherwise.

# Example 1:

# Input: s = "code"
# Output: false
# Example 2:

# Input: s = "aab"
# Output: true
# Example 3:

# Input: s = "carerac"
# Output: true
 

# Constraints:

# 1 <= s.length <= 5000
# s consists of only lowercase English letters.

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        elements = Counter(s)
        count_odds = 0
        for element,val in elements.items():
            if val %2 != 0:
                count_odds += 1
            if count_odds > 1:
                return False
        return True

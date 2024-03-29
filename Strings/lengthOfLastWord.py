# 58. Length of Last Word
# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word 
# if we loop from left to right) in the string.

# If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        w = s.split()
        if not w:
            return 0
        return len(w[-1])


# 151. Reverse Words in a String
# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

# Two pointer solution with O(n) space
class Solution:
    def reverseWords(self, s: str) -> str:
      s = s.strip()
      s = re.sub(r'\s+', ' ', s)
      prev = l = len(s)-1
      rev = ""
      while l>=0:
          if s[l] == " ":
              rev += s[l+1:prev+1]
              rev += " "
              prev = l-1
          l -= 1
      rev += s[l+1:prev+1]
      return rev
      
# One liner with builtin functions and no extra spaces
class Solution:
    def reverseWords(self, s: str) -> str:
      return " ".join(s.strip().split()[::-1]) 

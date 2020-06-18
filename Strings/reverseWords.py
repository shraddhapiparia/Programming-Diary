# 557. Reverse Words in a String III
# Given a string, you need to reverse the order of characters in each word within a 
# sentence while still preserving whitespace and initial word order.
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

# WORST SOLUTION EVER
class Solution:
    def reverseWords(self, s: str) -> str:
        start, newstr = 0, ""
        if not s:
            return s
        for i in range(len(s)):
            if s[i] == ' ':
                last = i
                for idx in reversed(range(start,last)):
                    newstr += s[idx]
                newstr += " "
                start = i + 1
        last = i+1
        for idx in reversed(range(start,last)):
            newstr += s[idx]
        return newstr
    
# Improved solution
class Solution:
    def reverseWords(self, s: str) -> str:
        start, newstr = 0, ""
        if not s:
            return s
        for n in s.split(" "):
            newstr += n[::-1] + " "
        return newstr[:-1]

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        val = ''
        for st in s:
            st = st.lower()
            if (ord(st) > 96 and ord(st) < 123) or (ord(st) > 47 and ord(st) < 58):
                l += 1
                val += st
        for i in range(l//2):
            if val[i] != val[l-i-1]:
                return False
        return True
        
# Valid Palindrome
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases. Note: For the purpose of this problem, we define empty string as valid palindrome.

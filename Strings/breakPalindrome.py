# 1328. Break a Palindrome. Given a palindromic string palindrome, replace exactly one character by any lowercase English letter so that the string becomes the lexicographically smallest possible string that isn't a palindrome.

# After doing so, return the final string.  If there is no way to do so, return the empty string.

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) ==1:
            return ""
        for i in range(len(palindrome)//2):
            if palindrome[i] != "a":
                return palindrome[:i]+"a"+palindrome[i+1:]
        i = len(palindrome) 
        return palindrome[:i-1]+"b"
        
        
 

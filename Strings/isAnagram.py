# 242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        total_set = set()
        for c in s:
            if c not in total_set:
                total_set.add(c)
                if s.count(c) != t.count(c):
                    return False
        return True
        
# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?        
        
from collections import defaultdict

# almost counting sort
def count_letters(string):
    letters = [0] * 26
    for i in range(len(string)):
        letters[ord(string[i]) - ord('a')] += 1
    return letters

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_s = count_letters(s)
        letters_t = count_letters(t)
        
        for i in range(26):
            if letters_s[i] != letters_t[i]:
                return False
            
        return True

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        exist = set()
        for c in ransomNote:
            if c not in exist:
                exist.add(c)
                if c not in magazine or ransomNote.count(c) > magazine.count(c):
                    return False
        return True
        
# 383 Leetcode        
#  Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

# Each letter in the magazine string can only be used once in your ransom note. 
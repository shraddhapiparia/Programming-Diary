class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        dicti, out = {}, -1
        if dicti[s[out]] > 1:
            out = -1 
        for c in s:
            dicti[c] = dicti[c] + 1 if c in dicti else 1
        for i in range(len(s)):
            if dicti[s[i]] == 1:
                return i
        return -1

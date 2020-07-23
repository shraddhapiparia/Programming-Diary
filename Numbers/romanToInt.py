#13. Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        i = 0
        while i < len(s):
            ss = 0
            if i+1 < len(s) and hashmap[s[i+1]] > hashmap[s[i]]:
                ss = hashmap[s[i+1]] - hashmap[s[i]]
                i += 2
            else:
                ss = hashmap[s[i]]
                i += 1
            val += ss
        return val
        
# Time and Space Complexity: O(1)

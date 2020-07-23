# 12. Integer to Roman

class Solution:
    def intToRoman(self, num: int) -> str:
        hashmap = {'I':1,'IV':4, 'V':5,'IX':9, 'X':10,'XL': 40, 'L':50,'XC':90, 'C':100,'CD':400, 'D':500,'CM':900,'M':1000}
        res,ch = "", ""
        while num > 0:
            for val in hashmap:
                m = 0
                if num >= hashmap[val]:
                    m = hashmap[val]
                    ch = val
            res += ch
            num = num - hashmap[ch]
        return res
        
# O(1) Time and Space

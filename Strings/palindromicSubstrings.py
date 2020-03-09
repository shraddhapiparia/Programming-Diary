class Solution:
    def countSubstrings(self, s: str) -> int:
        l, ans = len(s), 0
        for i in range(l):
            for a,b in [(i,i),(i,i+1)]:
                while a >= 0 and b < l and s[a] == s[b]:
                    a -= 1
                    b += 1
                ans += (b-a)//2
        return ans

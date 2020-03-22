class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        k = i = 0
        for j in range(len(haystack) - len(needle) + 1):  // Important: This loop reduction helps in solving TLE
            if haystack[j:j+len(needle)] == needle:
                return j
        return -1
  
# Without slicing takes more time  
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        k = i = 0
        for j in range(len(haystack) - len(needle) + 1):
        if needle[i] == haystack[j]:
                k = 1
                while i+k < len(needle) and j+k < len(haystack) and needle[i+k] == haystack[j+k]:
                    k += 1
            if k == len(needle):
                return j
        return -1

# 168. Excel Sheet Column Title
# Given a positive integer, return its corresponding column title as appear in an Excel sheet.

class Solution:
    def convertToTitle(self, n: int) -> str:
        s = ""
        while n > 0:
            if n % 26 == 0:
                s = "Z" + s
                n = n//26 - 1
            else:
                s = chr((n%26) + 64) + s
                n = n//26
        return s
        
class Solution:
    def convertToTitle(self, n: int) -> str:
        ans = ''
        while n:
            x = (n-1)%26
            ans += chr(65+x)
            n = (n-1)//26
        return ans[::-1]

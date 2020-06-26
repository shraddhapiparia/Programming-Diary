# 67. Add Binary. Given two binary strings, return their sum (also a binary string).

# The input strings are both non-empty and contains only characters 1 or 0.

# Convert to integer and add and covert it back to binary.
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        asum, res, i = 0, '', 0
        if a == "0" and b == "0":
            return "0"
        for s in a[::-1]:
            asum += int(s) * pow(2,i)
            i+=1
        i = 0
        for st in b[::-1]:
            asum += int(st) * pow(2,i)
            i+=1
        while asum:
            asum, r = asum//2, asum%2
            res += str(r)
        return res[::-1]
        

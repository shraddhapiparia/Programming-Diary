# 415. Add Strings: Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

# Note:

'''    The length of both num1 and num2 is < 5100.
    Both num1 and num2 contains only digits 0-9.
    Both num1 and num2 does not contain any leading zero.
    You must not use any built-in BigInteger library or convert the inputs to integer directly. '''

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j, c, result = len(num1)-1, len(num2)-1, 0, ""
        while i >=0 or j >= 0:
            x1 = int(num1[i]) if i >= 0 else 0
            x2 = int(num2[j]) if j >= 0 else 0
            s = c + x1 + x2
            c, s = s//10, s%10
            result = str(s) + result
            i -= 1
            j -= 1
        if c > 0: result = str(c) + result
        return result
        
# Time complexity: O(max(len(n1),len(n2)))
# Space complexity: O(n1+n2)

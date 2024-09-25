# 9. Palindrome Number
# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

# Constraints:

# -231 <= x <= 231 - 1
 

# Follow up: Could you solve it without converting the integer to a string?


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        xstr = str(x)
        n = len(xstr)
        for i in range(0,n//2):
            if xstr[i] != xstr[n-i-1]:
                return False
        return True

# FOLLOW UP
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        n = x
        new = 0
        while n>0:
            rem = n%10
            new = new*10 + rem
            n = n//10
        return new==x

# More efficient follow up: CHECK HALF NUMBER ONLY
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        new = 0
        while x>new:
            rem = x%10
            new = new*10 + rem
            x = x//10
        return new==x or new//10 ==x

# 367. Given a positive integer num, write a function which returns True if num is a perfect square else False.

# Note: Do not use any built-in library function such as sqrt.

# Newton's method:

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        i = num//2
        while i*i > num:
            i = (i+num//i)//2
        return i*i == num
        
# Binary Search

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        lo,hi = 2, num//2
        while lo <= hi:
            x = lo + (hi-lo) //2
            guess = x * x
            if guess == num:
                return True
            if guess > num:
                hi = x - 1
            else:
                lo = x + 1
        return False

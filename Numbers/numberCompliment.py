# 476. Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.
class Solution:
    def findComplement(self, num: int) -> int:
        quo, rem, s = num//2, num%2, 0
        res = '1' if rem == 0 else '0'
        while quo > 0:
            quo, rem = quo//2, quo%2
            res = '1' + res if rem == 0 else '0' + res
        l = len(res)
        for i in range(l):
            if res[i] == '1':
                s += pow(2,l-i-1)
        return s
        
# Another easier approach:
class Solution:
    def findComplement(self, num: int) -> int:
        n, bit = num, 1
        while n:
            num = num ^ bit
            bit = bit << 1 # left shift to multiply by 2 and find that bit
            n = n >> 1     # right shift to divide by 2 and keep count of loop for original number
        return num

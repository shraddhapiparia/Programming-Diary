# 509. The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the 
# sum of the two preceding ones, starting from 0 and 1. That is,

# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), for N > 1.

# Given N, calculate F(N).

class Solution:
    def fib(self, N: int) -> int:
        fpp = 0
        fp = 1
        if N == 0:
            return fpp
        if N == 1:
            return fp
        for i in range(1,N):
            fc = fp + fpp
            fpp, fp = fp, fc
        return fc

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

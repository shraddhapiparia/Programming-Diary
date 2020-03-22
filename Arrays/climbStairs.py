class Solution:
    def climbStairs(self, n: int) -> int:
        f_1 = 1
        f_2 = 2
        if n == 0:
            return None
        if n == 1:
            return f_1
        if n == 2:
            return f_2
        for i in range(2,n):
            f_c = f_1 + f_2
            f_1, f_2 = f_2, f_c
        return f_c

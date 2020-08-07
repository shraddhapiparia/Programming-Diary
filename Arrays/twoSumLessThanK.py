# 1099. Two Sum Less Than K. Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        ma = -1
        A = sorted(A)
        start, end = 0, len(A)-1
        while start < end:
            if (A[start] + A[end]) < K:
                s = A[start] + A[end]
                #print(A[start], A[end], start, end)
                ma = s if s > ma else ma
                start += 1
            else:
                end -= 1
        return ma
# O(log(n))

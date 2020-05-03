class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        lo, hi = 0, len(A)-1
        while lo <= hi:
            mid = lo + (hi-lo)//2
            if A[mid] >= A[mid+1]:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo
# Let's call an array A a mountain if the following properties hold:

    # A.length >= 3
    # There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]

# Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

# 989. Add to Array-Form of Integer. For a non-negative integer X, the array-form of X is an array of its digits in left to right order.  
# For example, if X = 1231, then the array form is [1,2,3,1].

# Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.

class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        res = []
        i, c = len(A) - 1, 0
        while i >= 0 or K:
            x1 = A[i] if i >= 0 else 0
            x2 = K%10 if K else 0
            s = c + x1 + x2
            c = s//10
            s = s%10
            K = K//10
            res.append(s)
            i -= 1
        if c > 0: res.append(c)
        return res[::-1]
        
# Time complexity: O(max(N,logK))
# Space complexity: O(max(N,logK))

# OR Add K to last digit of array and process it

class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        res = []
        i, c = len(A) - 1, 0
        A[i] += K
        while i >= 0 or c:
            x = A[i] if i >= 0 else 0
            s = c + x
            c = s//10
            s = s%10
            K = K//10
            res.append(s)
            i -= 1
        if c > 0: res.append(c)
        return res[::-1]

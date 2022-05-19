# 461. Hamming Distance EASYYY

# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given two integers x and y, return the Hamming distance between them.

 

# Example 1:

# Input: x = 1, y = 4
# Output: 2
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# The above arrows point to positions where the corresponding bits are different.
# Example 2:

# Input: x = 3, y = 1
# Output: 1

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_values, y_values = [], []
        dist = 0
        while x >= 1:
            x_values.append(x%2)
            x >>= 1
        while y >= 1:
            y_values.append(y%2)
            y >>= 1
        diff = len(x_values) if len(x_values) < len(y_values) else len(y_values)
        for i in range(diff):
            if(x_values[i] != y_values[i]):
                dist += 1
        if len(x_values) < len(y_values):
            dist += sum(y_values[diff:])
        else:
            dist += sum(x_values[diff:])
        return dist


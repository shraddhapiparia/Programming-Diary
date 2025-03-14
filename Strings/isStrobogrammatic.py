# 246. Strobogrammatic Number
# Given a string num which represents an integer, return true if num is a strobogrammatic number.

# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

# Example 1:
# Input: num = "69"
# Output: true
# Example 2:
# Input: num = "88"
# Output: true
# Example 3:
# Input: num = "962"
# Output: false

# Constraints:
# 1 <= num.length <= 50
# num consists of only digits.
# num does not contain any leading zeros except for zero itself.

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        key = {'6':'9', '8':'8', '9':'6','1':'1','0':'0'}
        start, end = 0, len(num)-1
        while start <= end:
            if num[start] not in key or num[end] not in key:
                return False
            elif key[num[start]] != num[end]:
                return False
            start += 1
            end -= 1
        return True

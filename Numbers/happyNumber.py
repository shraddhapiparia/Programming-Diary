class Solution:
    def isHappy(self, n: int) -> bool:
        res, arr, dicti = 0, [], {0:0, 1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64,9:81}
        while n != 1:
            if n not in arr:
                arr.append(n)
            else:
                return False
            res = 0
            while n != 0:
                dig = n%10
                res += dicti[dig]
                n = n//10
            n = res
        return True
 #202. Happy Number
 #Write an algorithm to determine if a number is "happy". A happy number is a number defined by the following process: S
 # tarting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until 
 # the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this 
 # process ends in 1 are happy numbers.

# Solution 2:
class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, n
        while True:
            slow = sum(int(c)**2 for c in str(slow))
            fast = sum(int(c)**2 for c in str(fast))
            fast = sum(int(c)**2 for c in str(fast))
            
            if slow == 1 or fast == 1:
                return True
            elif slow == fast:
                return False
        return True
# First solution seems mroe effective than above but this one has TC of O(n)

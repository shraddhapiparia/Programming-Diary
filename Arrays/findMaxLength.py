''' Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1. 
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
'''
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashmap, count, maxlen = {0:-1}, 0, 0
        for idx, n in enumerate(nums):
            count = count - 1 if n == 0 else count + 1
            if count not in hashmap:
                hashmap[count] = idx
            else:
                maxlen = idx - hashmap[count] if idx - hashmap[count] > maxlen else maxlen
        return maxlen

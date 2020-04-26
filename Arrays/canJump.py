class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)-1
        for i in reversed(range(l)):
            l = i if i+nums[i] >= l else l
        return l == 0
# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Determine if you are able to reach the last index.

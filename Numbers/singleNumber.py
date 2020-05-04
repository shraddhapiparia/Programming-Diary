# 136 Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dicti ={}
        for i in range(len(nums)):
            dicti[nums[i]] = dicti[nums[i]] + 1 if nums[i] in dicti else 1
        for item in dicti:
            if dicti[item] == 1:
                return item

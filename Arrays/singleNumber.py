class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dicti ={}
        for i in range(len(nums)):
            dicti[nums[i]] = dicti[nums[i]] + 1 if nums[i] in dicti else 1
        for item in dicti:
            if dicti[item] == 1:
                return item

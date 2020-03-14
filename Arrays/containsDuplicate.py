class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            if i+k < len(nums) and nums[i] == nums[i+k]:
                return True
        return False

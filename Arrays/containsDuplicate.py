# Below code fails for new testcases that have been added recently:
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            if i+k < len(nums) and nums[i] == nums[i+k]:
                return True
        return False
# This one works but probably more efficient solution exist
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for i,num in enumerate(nums):
            if num in hashmap and abs(hashmap[num]-i) <= k:
                    return True
            hashmap[num] = i
        return False

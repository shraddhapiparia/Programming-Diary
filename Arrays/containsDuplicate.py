# Below code fails for new testcases that have been added recently:
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            if i+k < len(nums) and nums[i] == nums[i+k]:
                return True
        return False
# This one works but need to find more efficient solution
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen, hashmap = set(), {}
        for i,num in enumerate(nums):
            if num not in seen:
                seen.add(num)
                hashmap[num] = i
            else:
                if abs(hashmap[num]-i) <= k:
                    return True
                else:
                    hashmap[num] = i
        return False

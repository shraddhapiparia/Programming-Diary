class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr1 = ptr2 = count = 0
        while ptr2 < len(nums):
            if nums[ptr1] != nums[ptr2]:
                ptr1 += 1
                nums[ptr1] = nums[ptr2]
                count += 1
            ptr2 += 1
        return count + 1

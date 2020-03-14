class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, hi = 0, len(nums) - 1
        while(low <= hi):
            mid = low + (hi-low)// 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < nums[hi]:
                if nums[hi] >= target and target > nums[mid]:
                    low = mid + 1
                else:
                    hi = mid - 1
            else:
                if target >= nums[low] and nums[mid] > target:
                    hi = mid -1
                else:
                    low = mid+1
        return -1

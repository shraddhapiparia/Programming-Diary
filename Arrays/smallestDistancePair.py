# 719. Find K-th Smallest Pair Distance

# The distance of a pair of integers a and b is defined as the absolute difference between a and b.
# Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

# Example 1:
# Input: nums = [1,3,1], k = 1
# Output: 0
# Explanation: Here are all the pairs:
# (1,3) -> 2
# (1,1) -> 0
# (3,1) -> 2
# Then the 1st smallest distance pair is (1,1), and its distance is 0.

# Example 2:
# Input: nums = [1,1,1], k = 2
# Output: 0

# Example 3:
# Input: nums = [1,6,1], k = 3
# Output: 5
 

# Constraints:

# n == nums.length
# 2 <= n <= 104
# 0 <= nums[i] <= 106
# 1 <= k <= n * (n - 1) / 2

class Solution:
    def kSmallerValues(self, nums,k,mid):
        count = 0
        left = 0
        # Count the number of pairs with distance <= mid
        for right in range(len(nums)):
            while nums[right] - nums[left] > mid:
                left += 1
            count += right - left
        return count >= k

    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        lo, hi = 0, nums[-1] - nums[0]
        res = 0
        while lo <= hi:
            mid = lo + (hi-lo)//2
            if self.kSmallerValues(nums, k, mid):
                res = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return res
        

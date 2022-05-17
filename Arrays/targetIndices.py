# 2089. Find Target Indices After Sorting Array EASYYY

# You are given a 0-indexed integer array nums and a target element target.

# A target index is an index i such that nums[i] == target.

# Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

 

# Example 1:

# Input: nums = [1,2,5,2,3], target = 2
# Output: [1,2]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The indices where nums[i] == 2 are 1 and 2.

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        val = []
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)):
            if sorted_nums[i] == target:
                val.append(i)
        return(val)

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        n_lower = n_target = 0
        for n in nums:
            if n < target:
                n_lower += 1
            elif n == target:
                n_target += 1
        return list(range(n_lower, n_lower + n_target)) if n_target else []
        

# 15. 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

# Solution 1 which gives TLE and 308/313 Test cases accepted. Try a binary Search for optimization.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        snums = sorted(nums)
        triplets = set()
        n = len(nums)
        for i in range(n-2):
            if i > 0 and snums[i] == snums[i - 1]:  # Skip duplicate values for i
                continue
            for j in range(i+1,n-1):
                if j > i + 1 and snums[j] == snums[j - 1]:  # Skip duplicate values for j
                    continue
                tsum = snums[i]+snums[j]
                if -tsum in snums[j + 1:]:
                    k = snums.index(-tsum, j + 1)
                    triplet = (snums[i], snums[j], snums[k])
                    triplets.add(triplet)
        return [list(triplet) for triplet in triplets]



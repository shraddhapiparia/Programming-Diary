1365. How Many Numbers Are Smaller Than the Current Number EASY

Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

Example 1:

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
Example 2:

Input: nums = [6,5,4,8]
Output: [2,1,0,3]
  
# This one beats 84%  
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        dup, out = 0, []
        output_dict = {sorted_nums[0]:0}
        for i in range(1,len(sorted_nums)):
            if (sorted_nums[i] == sorted_nums[i-1]):
                dup += 1
            else:
                output_dict[sorted_nums[i]] = output_dict[sorted_nums[i-1]]+1+dup
                dup = 0
        for val in nums:
            out.append(output_dict[val])
        return out

# A little simpler but slower output 65%
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sort_nums = sorted(nums)
        res = []
        for i in nums:
            res.append(sort_nums.index(i))
        return res  

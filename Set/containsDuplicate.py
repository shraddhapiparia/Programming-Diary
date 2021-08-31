# 217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h = set() #using array gives time exceeded error
        for num in nums:
            if num not in h:
                h.add(num)
            else:
                return True
        return False
      
# One liner:
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
            

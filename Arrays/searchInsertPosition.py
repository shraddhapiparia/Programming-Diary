class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1       
        if not nums:
            return 0
        if target<=nums[0]:
            return l
        elif target > nums[-1]:
            return r+1
        elif target== nums[-1]:
            return r
        
        while l<r:
            mid = l + (r-l)//2
            val = nums[mid]
            if target<val:
                r = mid
            elif target > val:
                l = mid
            else:
                return mid
            if l+1==r:                
                return l+1

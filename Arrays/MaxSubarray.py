def maxSubarray(nums):
    if not nums:
        print("Array does not exists")
    res = nums[0]
    sum = res 
    for n in nums[1:]:
        sum = n if sum < 0 else sum + n
        res = max(res,sum)
    print(res)
    
maxSubarray([-2,2,-1,4,3,-2,3,-2,-6])

#O(1) space complexity for constant number of variables
#O(n) time complexity for traversing the array

def sumTwo(nums, target):
    h = {}
    for i in range(len(nums)):
        if target - nums[i] not in h:
            h[nums[i]] = i
        else: 
            print([h[target-nums[i]],i])
            return
    print("Element not found")
    
sumTwo([1,2,1,4,5,4],5)

#O(n) space and time

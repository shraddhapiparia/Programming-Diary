def findMajority(nums):
    num_dict = {}
    l = len(nums)/2
    for i in nums:
        num_dict[i] = num_dict[i]+1 if i in num_dict else 1
        if (num_dict[i] > l):
            print(i,num_dict[i])
            return
        
findMajority([1,1,2,1,1,1,2,3,2,2,2,2,2,2,2,2,2])

#O(n) time to traverse the array, O(1) space to save constant number of variables

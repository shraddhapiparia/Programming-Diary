import heapq
def kthLargestElem(nums,k):
        heapq.heapify(nums)
        for i in range(len(nums) - k):
            heapq.heappop(nums)
        print(heapq.heappop(nums))
    
kthLargestElem([1,4,2,6,3],2)

#https://leetcode.com/problems/kth-largest-element-in-an-array

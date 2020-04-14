# Approach 1 O(N^2)
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def max_stones():
            max_index = stones.index(max(stones))
            stones[max_index], stones[-1] = stones[-1], stones[max_index]
            return stones.pop()
        
        while len(stones) > 1:
            stone1 = max_stones()
            stone2 = max_stones()
            if stone1 != stone2:
                stones.append(stone1-stone2)
        
        return stones[0] if stones else 0
        
# Approach 2 using heap O(NlogN)
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)
             
        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            if stone1 != stone2:
                heapq.heappush(stones, stone1-stone2)
        
        return -heapq.heappop(stones) if stones else 0
        
# Approach 3 Bucket sort

//Write after done

# 1046. We have a collection of stones, each stone has a positive integer weight. Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

    #If x == y, both stones are totally destroyed;
    #If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.

#At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

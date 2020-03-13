class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minVal, maxVal = math.inf, 0
        if len(prices) == 0:
            return 0
        for i in range(len(prices)):
            if prices[i] < minVal:
                minVal = prices[i]
            elif prices[i] - minVal > maxVal:
                maxVal = prices[i] - minVal
        return maxVal

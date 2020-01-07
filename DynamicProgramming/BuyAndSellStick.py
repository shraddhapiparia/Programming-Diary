class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        mini = float('inf')
        val = 0
        maxprofit = 0
        for i, price in enumerate(prices):
            if price < mini:
                mini = price
            elif (price - mini) > maxprofit:
                maxprofit = price - mini
        return maxprofit

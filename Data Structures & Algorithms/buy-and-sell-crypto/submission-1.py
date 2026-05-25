class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: # cannot use `if prices is None`
            return 0
        max_profit = 0
        current_min = prices[0]
        for price in prices:
            max_profit = max(price - current_min, max_profit)
            current_min = min(price, current_min)
        return max_profit
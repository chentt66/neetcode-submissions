class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices is None:
            return 0
        max_profit = 0
        current_min = prices[0]
        for p in prices:
            max_profit = max(p - current_min, max_profit)
            current_min = min(p, current_min)
        return max_profit

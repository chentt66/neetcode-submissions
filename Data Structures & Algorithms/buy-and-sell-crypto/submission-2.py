class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        dp = [0] * n # dp[i]: 在第 0…i 天内完成至多一次买卖的最大利润
        min_price = [0] * n # min_price[i]: 第 0…i 天的最低价格
        min_price[0] = prices[0]
        for i in range(1, n):
            min_price[i] = min(min_price[i-1], prices[i])
            dp[i] = max(dp[i-1], prices[i] - min_price[i])
        return dp[n-1]
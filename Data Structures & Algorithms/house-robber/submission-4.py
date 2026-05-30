class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp_prev1 = 0
        dp_prev2 = 0
        for i in range(n):
            val = max(nums[i]+dp_prev2, dp_prev1)
            dp_prev2 = dp_prev1
            dp_prev1 = val
        return dp_prev1
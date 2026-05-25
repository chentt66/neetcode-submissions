class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_prod = [1] * n
        right_prod = [1] * n
        for i in range(1, n):
            left_prod[i] = left_prod[i-1] * nums[i-1]
            right_prod[n-1-i] = right_prod[n-i] * nums[n-i]
        # for i in range(n-2, -1, -1):
        #     right_prod[i] = right_prod[i+1] * nums[i+1]
        res = [0] * n
        for i in range(n):
            res[i] = left_prod[i] * right_prod[i]
        return res
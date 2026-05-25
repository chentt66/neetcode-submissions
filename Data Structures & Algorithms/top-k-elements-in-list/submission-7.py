class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        count = Counter(nums)
        n = len(nums)
        buckets = [ [] for _ in range(n+1)]
        for num, cnt in count.items():
            buckets[cnt].append(num)
        res = []
        for i in range(n, -1, -1):
            for num in buckets[i]:
                if len(res) == k:
                    return res
                res.append(num)
        return res
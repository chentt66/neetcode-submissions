class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        count = Counter(nums)
        min_heap = []
        import heapq
        for num, cnt in count.items():
            heapq.heappush(min_heap, (cnt, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [num for (cnt, num) in min_heap]
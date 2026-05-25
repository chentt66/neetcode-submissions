class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        import heapq
        min_heap = []
        for num, cnt in count.items():
            heapq.heappush(min_heap, (cnt, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [num for (cnt, num) in min_heap]

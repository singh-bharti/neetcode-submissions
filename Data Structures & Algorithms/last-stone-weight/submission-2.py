class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            firstV = -heapq.heappop(max_heap)
            secondV = -heapq.heappop(max_heap)

            if firstV >= secondV:
                heapq.heappush(max_heap, -(firstV - secondV))
        return -max_heap[0] if max_heap else 0
        
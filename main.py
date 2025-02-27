import heapq
from typing import List

def _heappush_max(heap, item):
    # https://discuss.python.org/t/make-max-heap-functions-public-in-heapq/16944/8
    """Maxheap version of a heappush."""
    heap.append(item)
    heapq._siftdown_max(heap, 0, len(heap) - 1)


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq._heapify_max(stones)

        while len(stones) > 1:
            h1 = heapq._heappop_max(stones)
            h2 = heapq._heappop_max(stones)

            if h1 != h2:
                _heappush_max(stones, abs(h1 - h2))

        return stones[0] if stones else 0

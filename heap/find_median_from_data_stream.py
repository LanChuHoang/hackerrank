# https://leetcode.com/problems/find-median-from-data-stream/

import heapq


class MedianFinder:
    def __init__(self):
        # store 2 heaps
        # larger_heap (min heap) for the larger part of the arr
        # smaller_heap (max heap) for the smaller part of the arr
        self.larger_heap = []
        self.smaller_heap = []

    def addNum(self, num: int) -> None:
        if not self.larger_heap or num > self.larger_heap[0]:
            heapq.heappush(self.larger_heap, num)
        else:
            heapq.heappush(self.smaller_heap, num * -1)
        self._rebalance()

    def _rebalance(self):
        larger_len = len(self.larger_heap)
        smaller_len = len(self.smaller_heap)
        if smaller_len == larger_len or smaller_len + 1 == larger_len:
            return

        if smaller_len > larger_len:
            exchange = heapq.heappop(self.smaller_heap) * -1
            heapq.heappush(self.larger_heap, exchange)
        else:
            exchange = heapq.heappop(self.larger_heap) * -1
            heapq.heappush(self.smaller_heap, exchange)

    def findMedian(self) -> float:
        return (
            (self.larger_heap[0] + self.smaller_heap[0] * -1) / 2
            if len(self.larger_heap) == len(self.smaller_heap)
            else self.larger_heap[0]
        )

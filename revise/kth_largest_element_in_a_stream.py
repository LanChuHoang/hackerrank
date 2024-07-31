# https://leetcode.com/problems/kth-largest-element-in-a-stream/description/

import heapq


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.heap = sorted(nums)[-k:]
        self.k = k

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
            return self.heap[0]

        if val <= self.heap[0]:
            return self.heap[0]

        heapq.heapreplace(self.heap, val)
        return self.heap[0]


# s = KthLargest(3, [4, 5, 8, 2])
# print(s.add(3))
# print(s.add(5))
# print(s.add(10))
# print(s.add(9))
# print(s.add(4))

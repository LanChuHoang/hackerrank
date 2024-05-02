# https://leetcode.com/problems/kth-largest-element-in-a-stream/description/

import heapq


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        # Init a min heap of size k to store k largest elements
        sorted_nums = sorted(nums)
        self.k = k
        self.k_largest_heap = sorted_nums[-self.k :]

    def add(self, val: int) -> int:
        # if the heap is not full -> add new element -> return top
        if len(self.k_largest_heap) < self.k:
            heapq.heappush(self.k_largest_heap, val)
        # else compare the new val with the smallest element of the k largest heap (the top one)
        # if the new val > the top, remove the top of the heap, add the new val to the heap
        elif val > self.k_largest_heap[0]:
            heapq.heapreplace(self.k_largest_heap, val)

        return self.k_largest_heap[0]


k_largest = KthLargest(k=3, nums=[5, -1])
print(k_largest.k_largest_heap)
print(k_largest.add(2))

# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        k_largest_nums = []
        for num in nums:
            if len(k_largest_nums) < k:
                heapq.heappush(k_largest_nums, num)
            elif num > k_largest_nums[0]:
                heapq.heapreplace(k_largest_nums, num)
        return k_largest_nums[0]

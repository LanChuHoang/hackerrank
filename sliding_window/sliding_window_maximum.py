# https://leetcode.com/problems/sliding-window-maximum/

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        start, end = 0, k - 1
        result = []
        stack = deque()
        for i in range(end + 1):
            while stack and stack[0] < 
        while True:
            print(window)
            max_window = heapq.heappop(window)
            result.append(max_window * -1)

            if max_window == nums[start]:
                heapq.heappush(window, max_window)
            start += 1

            end += 1
            if end >= len(nums):
                break

            heapq.heappush(window, nums[end])

        return result

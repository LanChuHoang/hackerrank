# https://leetcode.com/problems/sliding-window-maximum/

import heapq


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        start, end = 0, k - 1

        window = nums[start : end + 1]
        heapq._heapify_max(window)

        result = []
        while True:
            print(window)
            max_item = window[0]
            result.append(max_item)
            start += 1
            end += 1
            if end >= len(nums):
                break
            if nums[start] == window[0]:
                print("remove")
                heapq._heappop_max(window)
            heapq.heappush(window, nums[end])
            print(window)

        return result


print(Solution().maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))

# https://leetcode.com/problems/sliding-window-maximum/

from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        stack = deque()
        l, r, n = 0, 0, len(nums)
        res = []
        while r < k:
            while stack and stack[-1] < nums[r]:
                stack.pop()
            stack.append(nums[r])
            r += 1

        while r < n:
            res.append(stack[0])
            # reduce left
            if nums[l] == stack[0]:
                stack.popleft()
            l += 1

            # expand right
            while stack and stack[-1] < nums[r]:
                stack.pop()
            stack.append(nums[r])
            r += 1
        res.append(stack[0])
        return res


# s = Solution()
# print(s.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
# print(s.maxSlidingWindow(nums=[1], k=1))

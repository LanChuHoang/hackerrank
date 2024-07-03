# https://leetcode.com/problems/largest-rectangle-in-histogram/

from collections import deque


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        prev_smallers = [0 for _ in range(n)]
        next_smallers = [0 for _ in range(n)]
        stack = deque()

        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                idx = stack.pop()
                next_smallers[idx] = i
            stack.append(i)
        while stack:
            idx = stack.pop()
            next_smallers[idx] = n

        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] > heights[i]:
                idx = stack.pop()
                prev_smallers[idx] = i
            stack.append(i)
        while stack:
            idx = stack.pop()
            prev_smallers[idx] = -1

        result = 0
        for i in range(n):
            result = max(
                result,
                heights[i],
                heights[i] * (next_smallers[i] - prev_smallers[i] - 1),
            )
        return result


# s = Solution()
# print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))

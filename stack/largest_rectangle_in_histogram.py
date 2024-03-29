# https://leetcode.com/problems/largest-rectangle-in-histogram/description/

from collections import deque


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        next_smaller_stack = deque()
        prev_smaller_stack = deque()
        next_smaller_index = [len(heights)] * len(heights)
        prev_smaller_index = [-1] * len(heights)
        for i in range(len(heights)):
            while next_smaller_stack and heights[i] < next_smaller_stack[-1][0]:
                _, index = next_smaller_stack.pop()
                next_smaller_index[index] = i
            next_smaller_stack.append((heights[i], i))
        for i in range(len(heights) - 1, -1, -1):
            while prev_smaller_stack and heights[i] < prev_smaller_stack[-1][0]:
                _, index = prev_smaller_stack.pop()
                prev_smaller_index[index] = i
            prev_smaller_stack.append((heights[i], i))
        max_area = 0
        for i, h in enumerate(heights):
            cur_area = h * (next_smaller_index[i] - prev_smaller_index[i] - 1)
            max_area = max(max_area, cur_area)
        return max_area

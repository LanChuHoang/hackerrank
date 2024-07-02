# https://leetcode.com/problems/daily-temperatures/

from collections import deque

# Idea: create a non decreasing stack act like a wating queue to store dates
# that not found any corresponding warmer dates yet. So every time we found a warmer date, which is a date that
# > the top of the stack, then we pop the stack for every date that < the warmer date and keep doing that
# Insight: multiple dates can have the same nearest warmer date


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result = [0] * len(temperatures)
        stack = deque()

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                _, index = stack.pop()
                result[index] = i - index

            stack.append((temperatures[i], i))

        return result

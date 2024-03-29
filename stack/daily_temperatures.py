# https://leetcode.com/problems/daily-temperatures/

from collections import deque


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

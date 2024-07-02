# https://leetcode.com/problems/daily-temperatures/

from collections import deque


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result = [0] * len(temperatures)
        waiting_stack = deque()
        for i in range(len(temperatures)):
            while waiting_stack and waiting_stack[-1][0] < temperatures[i]:
                idx = waiting_stack.pop()[1]
                result[idx] = i - idx
            waiting_stack.append((temperatures[i], i))
        return result

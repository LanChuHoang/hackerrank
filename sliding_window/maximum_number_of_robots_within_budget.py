# https://leetcode.com/problems/maximum-number-of-robots-within-budget/

from collections import deque


class Solution:
    def maximumRobots(
        self, chargeTimes: list[int], runningCosts: list[int], budget: int
    ) -> int:
        # Idea: maintain a non-increasing stack to get the next max of chargeTimes
        # Expand the window until it hits the break point (> budget)
        # then recude it down and repeat
        l, r, n = 0, 0, len(chargeTimes)
        res = 0
        cur_sum = runningCosts[l]
        stack = deque()
        stack.append(chargeTimes[l])
        while r < n:
            cur_max = stack[0]
            wlen = r - l + 1
            cur_cost = cur_max + wlen * cur_sum
            if cur_cost <= budget:
                res = max(res, wlen)
                r += 1

                if r < n:
                    while stack and stack[-1] < chargeTimes[r]:
                        stack.pop()
                    stack.append(chargeTimes[r])
                    cur_sum += runningCosts[r]
            else:
                if chargeTimes[l] == stack[0]:
                    stack.popleft()
                cur_sum -= runningCosts[l]
                l += 1
                if l > r:
                    r += 1
                    if r < n:
                        stack.append(chargeTimes[r])
                        cur_sum = runningCosts[r]
        return res


# s = Solution()
# print(
#     s.maximumRobots(
#         chargeTimes=[3, 6, 1, 3, 4], runningCosts=[2, 1, 3, 4, 5], budget=25
#     )
# )
# print(s.maximumRobots(chargeTimes=[11, 12, 19], runningCosts=[10, 8, 7], budget=19))

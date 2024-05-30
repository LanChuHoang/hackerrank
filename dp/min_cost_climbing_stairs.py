# https://leetcode.com/problems/min-cost-climbing-stairs/description/

"""
min(i) = min(min(i-1) + cost[i-1], min(i-2) + cost[i-2])
min cost at i is min of
 - min cost to reach i - 1 + cost[i-1]
 or min cost to reach i - 2 + cost[i-2]
"""


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        min_prev_1, min_prev_2 = 0, 0
        for i in range(2, len(cost) + 1):
            cur_min = min(min_prev_1 + cost[i - 1], min_prev_2 + cost[i - 2])
            min_prev_2 = min_prev_1
            min_prev_1 = cur_min

        return cur_min


# print(Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))

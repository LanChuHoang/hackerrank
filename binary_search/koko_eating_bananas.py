# https://leetcode.com/problems/koko-eating-bananas/
import math


class Solution:
    def cal_hours(self, piles: list[int], speed: int):
        total_hours = 0
        for p in piles:
            total_hours += math.ceil(p / speed)
        return total_hours

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        i, j = 1, max(piles)

        res = j

        while i <= j:
            mid = (i + j) // 2
            hours = self.cal_hours(piles, mid)

            if hours <= h:
                res = min(mid, res)
                j = mid - 1
            else:
                i = mid + 1

        return res


# print(Solution().minEatingSpeed([1, 1, 1, 999999999], h=10))

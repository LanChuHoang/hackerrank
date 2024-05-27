# https://leetcode.com/problems/koko-eating-bananas/

import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        max_bananas = max(piles)
        l, r = 1, max_bananas

        while l <= r:
            m = (l + r) // 2
            cost = 0
            for num_b in piles:
                cost += math.ceil(num_b / m)

            if cost <= h:
                r = m - 1
            else:
                l = m + 1

        return r + 1


piles = [312884470]

h = 312884469
print(Solution().minEatingSpeed(piles, h))

# https://leetcode.com/problems/k-closest-points-to-origin/

import heapq
import math


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = [(math.sqrt(p[0] ** 2 + p[1] ** 2), p) for p in points]
        heapq.heapify(heap)
        result = []
        i = 0
        while heap and i < k:
            result.append(heapq.heappop(heap)[1])
            i += 1

        return result

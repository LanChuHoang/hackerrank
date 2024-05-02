# https://leetcode.com/problems/last-stone-weight/description/

import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        inverse_stones = [s * -1 for s in stones]
        heapq.heapify(inverse_stones)

        while len(inverse_stones) > 1:
            first_weight = abs(heapq.heappop(inverse_stones))
            second_weight = abs(heapq.heappop(inverse_stones))
            if first_weight != second_weight:
                new_stone = first_weight - second_weight
                heapq.heappush(inverse_stones, new_stone * -1)

        return inverse_stones[0] * -1 if inverse_stones else 0

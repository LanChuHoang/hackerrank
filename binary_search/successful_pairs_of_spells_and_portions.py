# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/?envType=study-plan-v2&envId=binary-search


class Solution:
    def successfulPairs(
        self, spells: list[int], potions: list[int], success: int
    ) -> list[int]:
        n = len(spells)
        m = len(potions)
        potions.sort()

        result = [0 for _ in range(n)]
        for i in range(n):
            target = success / spells[i]

            left, right = 0, m - 1
            smallest_potion_idx = None
            while left <= right:
                mid = left + (right - left) // 2
                if potions[mid] >= target:
                    smallest_potion_idx = mid
                    right = mid - 1
                else:
                    left = mid + 1
            if smallest_potion_idx is not None:
                result[i] = m - smallest_potion_idx

        return result


# s = Solution()
# print(s.successfulPairs(spells=[5, 1, 3], potions=[1, 2, 3, 4, 5], success=7))
# print(s.successfulPairs(spells=[3, 1, 2], potions=[8, 5, 8], success=16))
# print(s.successfulPairs())

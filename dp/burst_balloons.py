# https://leetcode.com/problems/burst-balloons/description/


class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        nums = [1] + nums + [1]
        memo = dict()

        def dfs(l: int, r: int):
            if l > r:
                return 0

            if (l, r) in memo:
                return memo[(l, r)]

            memo[(l, r)] = 0
            for i in range(l, r + 1):
                coins = nums[i - 1] * nums[i] * nums[i + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                memo[(l, r)] = max(memo[(l, r)], coins)
            return memo[(l, r)]

        return dfs(1, len(nums) - 2)

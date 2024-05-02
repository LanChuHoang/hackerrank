# https://leetcode.com/problems/jump-game-ii/description/


class Solution:
    def jump(self, nums: list[int]) -> int:
        min_jumps = 0
        l, r = 0, 0
        while r < len(nums) - 1:
            max_reachable_idx = -1
            for i in range(l, r + 1):
                max_reachable_idx = max(max_reachable_idx, i + nums[i])
            l = r + 1
            r = max_reachable_idx
            min_jumps += 1

        return min_jumps

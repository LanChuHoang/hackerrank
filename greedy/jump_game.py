# https://leetcode.com/problems/jump-game/description/


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_can_jump_idx = 0
        for i, max_jump in enumerate(nums):
            if max_can_jump_idx < i:
                return False
            max_can_jump_idx = max(max_can_jump_idx, i + max_jump)

        return True

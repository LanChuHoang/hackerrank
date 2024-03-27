# https://leetcode.com/problems/trapping-rain-water/


class Solution:
    def trap(self, height: list[int]) -> int:
        max_left = [0] * len(height)
        max_right = [0] * len(height)
        result = 0

        for i in range(1, len(height)):
            max_left[i] = max(max_left[i - 1], height[i - 1])
        for i in range(len(height) - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i + 1])
        for i in range(len(height)):
            fillable_amount = min(max_left[i], max_right[i]) - height[i]
            result += max(fillable_amount, 0)

        return result

# https://leetcode.com/problems/trapping-rain-water/


class Solution:
    def trap(self, height: list[int]) -> int:
        max_left = [height[0]]

        for i in range(1, len(height)):
            if height[i] > max_left[i - 1]:
                max_left.append(height[i])
            else:
                max_left.append(max_left[i - 1])

        result = 0
        prev_max_right = height[-1]
        for i in range(len(height) - 2, -1, -1):
            cur_max_right = height[i] if height[i] > prev_max_right else prev_max_right
            result += min(cur_max_right, max_left[i]) - height[i]
            prev_max_right = cur_max_right

        return result

# https://leetcode.com/problems/container-with-most-water/description/


class Solution:
    def maxArea(self, height: list[int]) -> int:
        # Only shift the lower side, because if we shift the larger side
        # the area only decreases

        l, r = 0, len(height) - 1
        max_area = 0

        while l < r:
            if height[l] < height[r]:
                cur_area = (r - l) * height[l]
                l += 1
            else:
                cur_area = (r - l) * height[r]
                r -= 1
            max_area = max(max_area, cur_area)

        return max_area

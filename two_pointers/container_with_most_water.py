# https://leetcode.com/problems/container-with-most-water/
# Explaination: 7:25 - https://www.youtube.com/watch?v=5HU0iQ1wlMo


class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        i = 0
        j = len(height) - 1
        while i < j:
            area = min(height[i], height[j]) * (j - i)
            max_area = max(max_area, area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area

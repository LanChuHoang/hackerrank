# https://leetcode.com/problems/find-peak-element/?envType=study-plan-v2&envId=top-interview-150

# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        l, r = 1, len(nums) - 2
        while l < r:
            m = (l + r) // 2
            if nums[m - 1] <= nums[m] >= nums[m + 1]:
                return m
            elif nums[m] < nums[m + 1]:
                l = m + 1
            else:
                r = m
        return l

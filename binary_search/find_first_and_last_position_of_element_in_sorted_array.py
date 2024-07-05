# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)

        first_idx = -1
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                first_idx = m
                r = m - 1
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1

        last_idx = -1
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                last_idx = m
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return [first_idx, last_idx]


# s = Solution()
# print(s.searchRange([5, 7, 7, 8, 8, 10], target=8))
# print(s.searchRange(nums=[5, 7, 7, 8, 8, 10], target=6))
# print(s.searchRange(nums=[], target=0))

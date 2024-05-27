# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/


class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1

        result = nums[l]
        while l <= r and nums[l] > nums[r]:
            m = (l + r) // 2
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
            result = min(result, nums[l], nums[r], nums[m])

        return result


# print(Solution().findMin([3, 1, 2]))

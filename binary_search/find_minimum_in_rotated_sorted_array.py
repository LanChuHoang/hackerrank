# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/


class Solution:
    def findMin(self, nums: list[int]) -> int:
        min_num = nums[0]
        prev_mid = nums[0]

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if prev_mid <= nums[mid]:
                left = mid + 1
            else:
                min_num = min(min_num, nums[mid])
                right = mid - 1

        return min_num


print(Solution().findMin([5, 4, 3, 0, 1]))  # --> wrong, leetcode missed this case

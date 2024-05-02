# https://leetcode.com/problems/find-the-duplicate-number/


class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == i:
                return nums[i]
            next_index = nums[i]
            nums[i] = i
            i = next_index


print(Solution().findDuplicate([3, 1, 3, 4, 2]))

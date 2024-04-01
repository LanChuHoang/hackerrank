# https://leetcode.com/problems/search-in-rotated-sorted-array/


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            k = (i + j) // 2
            print(i, j, k, nums[k])
            if nums[k] == target:
                return k
            if nums[i] <= nums[k]:
                if nums[i] <= target < nums[k]:
                    j = k - 1
                else:
                    i = k + 1
            else:
                if nums[k] < target <= nums[j]:
                    i = k + 1
                else:
                    j = k - 1
        return -1


print(Solution().search([11, 13, 15, 10], 13))

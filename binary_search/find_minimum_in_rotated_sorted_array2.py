# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/?envType=study-plan-v2&envId=binary-search


class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m
            else:
                r -= 1
        return nums[l]


s = Solution()
print(s.findMin([4, 5, 6, 7, 0, 1, 4]))
print(s.findMin([0, 1, 4, 4, 5, 6, 7]))
print(s.findMin([1, 3, 5]))
print(s.findMin([2, 2, 2, 0, 1]))
print(s.findMin([3, 1]))
print(s.findMin([10, 1, 10, 10, 10]))

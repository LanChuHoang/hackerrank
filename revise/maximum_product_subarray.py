# https://leetcode.com/problems/maximum-product-subarray/


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n = len(nums)

        res, cur_max, cur_min = nums[-1], nums[-1], nums[-1]
        for i in range(n - 2, -1, -1):
            options = (nums[i], nums[i] * cur_max, nums[i] * cur_min)
            cur_max, cur_min = max(options), min(options)
            res = max(res, cur_max)
        return res


s = Solution()
print(s.maxProduct([2, 3, -2]))
print(s.maxProduct([-2, 0, -1]))
print(s.maxProduct([-3, -1, -1]))
print(s.maxProduct([-1, -2, -9, -6]))

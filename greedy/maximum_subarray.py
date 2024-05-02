# https://leetcode.com/problems/maximum-subarray/description/


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        cur_sum = nums[0]
        max_so_far = cur_sum
        for i in range(1, len(nums), 1):
            # If adding the nums[i] create a that > nums[i] alone -> continue expand the sum,
            # else -> make a new sum, because the prev sum is useless, adding it makes the sum worst
            cur_sum = max(cur_sum + nums[i], nums[i])
            max_so_far = max(cur_sum, max_so_far)
        return max_so_far

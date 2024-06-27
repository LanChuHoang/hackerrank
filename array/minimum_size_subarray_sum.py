# https://leetcode.com/problems/minimum-size-subarray-sum/?envType=study-plan-v2&envId=top-interview-150

# Expand the window to the right until the sum >= target, then decrease the sum by increasing the left
# until it < target, so we can insert new element to the window


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l, r = 0, 0
        cur_sum = 0

        result = len(nums) + 1
        while r < len(nums):
            cur_sum += nums[r]
            while l <= r and cur_sum >= target:
                result = min(result, r - l + 1)
                cur_sum -= nums[l]
                l += 1
            r += 1

        return result if result <= len(nums) else 0


# s = Solution()
# print(s.minSubArrayLen(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]))

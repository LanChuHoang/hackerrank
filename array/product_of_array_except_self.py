# https://leetcode.com/problems/product-of-array-except-self/description/


class Solution:

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [1] * len(nums)

        # Calculate left product of each element
        for i in range(1, len(nums), 1):
            result[i] = result[i - 1] * nums[i - 1]

        # Calculate right product of each element and multiply with left product
        prev_right_prod = 1
        for i in range(len(nums) - 2, -1, -1):
            cur_right_prod = prev_right_prod * nums[i + 1]
            result[i] *= cur_right_prod
            prev_right_prod = cur_right_prod

        return result

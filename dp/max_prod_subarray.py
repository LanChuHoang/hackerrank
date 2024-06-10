# https://leetcode.com/problems/maximum-product-subarray/


class Solution:
    def maxProduct_v1(self, nums: list[int]) -> int:
        max_prod = [n for n in nums]
        min_prod = [n for n in nums]

        for i in reversed(range(len(nums) - 1)):
            with_next_max = nums[i] * max_prod[i + 1]
            with_next_min = nums[i] * min_prod[i + 1]
            max_prod[i] = max(nums[i], with_next_max, with_next_min)
            min_prod[i] = min(nums[i], with_next_max, with_next_min)
        return max(max_prod)

    def maxProduct(self, nums: list[int]) -> int:
        max_prod = nums[-1]
        min_prod = nums[-1]
        result = max_prod
        for i in reversed(range(len(nums) - 1)):
            with_next_max = nums[i] * max_prod
            with_next_min = nums[i] * min_prod
            max_prod = max(nums[i], with_next_max, with_next_min)
            min_prod = min(nums[i], with_next_max, with_next_min)
            result = max(result, max_prod)
        return result


solution = Solution()
print(solution.maxProduct([2, 3, -2, 4]))
print(solution.maxProduct([-2, 0, -1]))
print(solution.maxProduct([-3, -1, -1]))
print(solution.maxProduct([-3, -1, -1, -2]))

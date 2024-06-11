# https://leetcode.com/problems/target-sum/


class Solution:
    def findTargetSumWays(self, nums: list[int], amount: int) -> int:
        # For every i and target
        # num_sols(i, target) = num_sols(i + 1, target + nums[i]) + num_sols(i + 1, target - nums[i])

        memo = dict()

        def num_sols(i: int, target: int):
            if i >= len(nums):
                return target == 0

            if (i, target) in memo:
                return memo[(i, target)]

            memo[(i, target)] = num_sols(i + 1, target + nums[i]) + num_sols(
                i + 1, target - nums[i]
            )
            return memo[(i, target)]

        return num_sols(0, amount)


s = Solution()
print(s.findTargetSumWays([1, 1, 1, 1, 1], 3))
print(s.findTargetSumWays([1], 1))

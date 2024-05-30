# https://leetcode.com/problems/house-robber/


class Solution:
    def max_rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        max_robable = [0 for _ in range(len(nums) + 1)]
        max_robable[-2] = nums[-1]
        max_robable[-3] = nums[-2]
        for i in reversed(range(len(max_robable) - 3)):
            max_robable[i] = max(max_robable[i + 2], max_robable[i + 3]) + nums[i]
        return max(max_robable[0], max_robable[1])

    def rob(self, nums: list[int]) -> int:
        return max(self.max_rob(nums[:-1]), self.max_rob(nums[1:]))


print(Solution().rob([1, 2, 3, 1]))

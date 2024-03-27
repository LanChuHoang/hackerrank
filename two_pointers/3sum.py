# https://leetcode.com/problems/3sum/description/


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sorted_nums = sorted(nums)
        result = set()

        for i in range(len(sorted_nums) - 1):
            j = i + 1
            k = len(sorted_nums) - 1
            while j < k:
                cur_sum = sorted_nums[i] + sorted_nums[j] + sorted_nums[k]
                if cur_sum == 0:
                    result.add((sorted_nums[i], sorted_nums[j], sorted_nums[k]))
                    j += 1
                    k -= 1
                elif cur_sum < 0:
                    j += 1
                else:
                    k -= 1

        return list(result)

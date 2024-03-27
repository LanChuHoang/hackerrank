# https://leetcode.com/problems/two-sum/description/


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_with_index = sorted(enumerate(nums), key=lambda x: x[1])
        i = 0
        j = len(nums) - 1
        while i < j:
            cur_sum = nums_with_index[i][1] + nums_with_index[j][1]
            if cur_sum == target:
                return [nums_with_index[i][0], nums_with_index[j][0]]
            elif cur_sum < target:
                i += 1
            else:
                j -= 1

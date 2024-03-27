# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            cur_sum = numbers[i] + numbers[j]
            if cur_sum == target:
                return [i + 1, j + 1]
            elif cur_sum < target:
                i += 1
            else:
                j -= 1

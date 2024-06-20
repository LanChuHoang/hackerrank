# https://leetcode.com/problems/longest-consecutive-sequence/description/


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)

        result = 0
        for num in num_set:
            if num - 1 in num_set:
                continue

            count = 1
            while num + count in num_set:
                count += 1
            result = max(result, count)

        return result

# https://leetcode.com/problems/longest-consecutive-sequence/description/


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        length = len(nums)
        if length < 2:
            return length
        num_set = set(nums)
        max_length = 0
        for num in num_set:
            if num - 1 not in num_set:
                cur_length = 1
                while num + 1 in num_set:
                    cur_length += 1
                    num += 1
                max_length = max(max_length, cur_length)
        return max_length

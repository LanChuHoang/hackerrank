# https://leetcode.com/problems/subsets-ii/description/


class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        num_count = dict()
        for n in nums:
            num_count[n] = num_count.get(n, 0) + 1

        unum = list(num_count.keys())
        n = len(unum)
        res = []
        cur_subset = []

        def dfs(i: int):
                

        dfs(0)
        return res

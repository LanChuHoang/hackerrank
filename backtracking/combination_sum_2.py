# https://leetcode.com/problems/combination-sum-ii/description/


class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates = sorted(candidates)
        result = []
        cur_sum = 0
        subset = []

        def dfs(i: int):
            nonlocal result, cur_sum, subset
            if cur_sum == target:
                result.append(subset.copy())
                return

            if i == len(candidates) or cur_sum > target:
                return

            # go left the tree, all subsets that include nums[i]
            subset.append(candidates[i])
            cur_sum += candidates[i]
            dfs(i + 1)
            cur_sum -= candidates[i]
            subset.pop()

            # go right the tree, not include nums[i], go to the next distinct element
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1)

        dfs(0)
        return result

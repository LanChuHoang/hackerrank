# https://leetcode.com/problems/combination-sum/description/


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        cur_sum = 0
        subset = []

        def dfs(idx: int):
            nonlocal result, cur_sum, subset

            if idx == len(candidates) or cur_sum > target:
                return

            if cur_sum == target:
                result.append(subset.copy())
                return

            # go left the tree, add the element c[i] to the combination
            subset.append(candidates[idx])
            cur_sum += candidates[idx]
            dfs(idx)

            # go right the tree, not include the element c[i] to the combination
            subset.pop()
            cur_sum -= candidates[idx]
            dfs(idx + 1)

        dfs(0)
        return list(result)


# print(Solution().combinationSum(candidates=[2, 3, 5], target=8))

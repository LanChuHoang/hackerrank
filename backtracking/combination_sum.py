# https://leetcode.com/problems/combination-sum/description/


class Solution:
    def combinationSum_v1(self, candidates: list[int], target: int) -> list[list[int]]:
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

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        # Idea: sort the candidate array to get away invalid parts
        # based on cur_sum. If at some candidate, we regonize that
        # the cur_sum is already larger that the target then we
        # dont need to consider all the larger candidates

        candidates.sort()

        res = []
        cur_combination = []
        n = len(candidates)

        def dfs(start: int, cur_sum: int):
            if cur_sum == target:
                res.append(cur_combination.copy())
                return

            for i in range(start, n):
                next_sum = cur_sum + candidates[i]
                if next_sum > target:
                    break
                cur_combination.append(candidates[i])
                dfs(i, next_sum)
                cur_combination.pop()

        dfs(0, 0)
        return res


# print(Solution().combinationSum(candidates=[2, 3, 5], target=8))

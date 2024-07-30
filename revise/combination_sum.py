# https://leetcode.com/problems/combination-sum/


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
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


# s = Solution()
# print(s.combinationSum([2, 3, 6, 7], 7))
# print(s.combinationSum(candidates=[2, 3, 5], target=8))
# print(s.combinationSum(candidates=[2], target=1))

# https://leetcode.com/problems/subsets/description/


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        subset = []

        def dfs(idx: int):
            nonlocal result, subset
            if idx == len(nums):
                result.append(subset.copy())
                return

            # go left the tree, without the current element in the subset
            dfs(idx + 1)

            # go right the tree, with the current element in the subset
            subset.append(nums[idx])
            dfs(idx + 1)

            # clean up to restore
            subset.pop()

        dfs(0)
        return result


print(Solution().subsets([1, 2, 3]))

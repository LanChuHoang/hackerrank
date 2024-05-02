# https://leetcode.com/problems/subsets-ii/description/


class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        result = []
        subset = []
        nums.sort()

        def dfs(idx: int):
            nonlocal result, subset
            if idx == len(nums):
                result.append(subset.copy())
                return

            # go left the tree, all subsets that include nums[i]
            subset.append(nums[idx])
            dfs(idx + 1)
            subset.pop()

            # go right the tree, all subsets that don't include nums[i]
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1
            dfs(idx + 1)

        dfs(0)
        return result

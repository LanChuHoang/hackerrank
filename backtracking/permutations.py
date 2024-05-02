# https://leetcode.com/problems/permutations/description/


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []

        permutation = []
        # key: modify the chosen recursively to create permutations
        chosen = [False] * len(nums)

        def dfs():
            nonlocal result, permutation, chosen

            if len(permutation) == len(nums):
                result.append(permutation.copy())
                return

            for i in range(len(nums)):
                if chosen[i]:
                    continue

                chosen[i] = True
                permutation.append(nums[i])
                dfs()
                chosen[i] = False
                permutation.pop()

        dfs()
        return result

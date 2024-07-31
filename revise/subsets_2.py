# https://leetcode.com/problems/subsets-ii/description/


class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        # Idea: Each unique number we have 2 choices
        # - choose this number, and take 1 or 2 or,...,count of that number
        # - dont choose this number

        num_count = dict()
        for n in nums:
            num_count[n] = num_count.get(n, 0) + 1

        unum = list(num_count.keys())
        n = len(unum)
        res = []
        cur_subset = []

        def dfs(i: int):
            if i == n:
                res.append(cur_subset.copy())
                return

            for _ in range(1, num_count[unum[i]] + 1):
                cur_subset.append(unum[i])
                dfs(i + 1)
            for _ in range(1, num_count[unum[i]] + 1):
                cur_subset.pop()

            dfs(i + 1)

        dfs(0)
        return res


# s = Solution()
# print(s.subsetsWithDup([1, 2, 2, 3]))

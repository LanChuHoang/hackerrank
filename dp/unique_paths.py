# https://leetcode.com/problems/unique-paths/description/


class Solution:
    def uniquePaths_v1(self, m: int, n: int) -> int:
        if m <= 1 or n <= 1:
            return 1

        def backtrack(i: int, j: int) -> int:
            if i == m - 1 and j == n - 1:
                return 1

            if i >= m or j >= n:
                return 0

            # number of paths at i, j = num_paths(i, j)
            # num_paths(i, j) = num_paths(i + 1, j) + num_paths(i, j + 1)

            return backtrack(i + 1, j) + backtrack(i, j + 1)

        return backtrack(0, 0)

    def uniquePaths_v2(self, m: int, n: int) -> int:
        if m <= 1 or n <= 1:
            return 1

        memo = dict()

        def backtrack(i: int, j: int) -> int:
            if i == m - 1 and j == n - 1:
                return 1

            if i >= m or j >= n:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            # number of paths at i, j = num_paths(i, j)
            # num_paths(i, j) = num_paths(i + 1, j) + num_paths(i, j + 1)

            num_paths = backtrack(i + 1, j) + backtrack(i, j + 1)
            memo[(i, j)] = num_paths
            return num_paths

        return backtrack(0, 0)

    def uniquePaths(self, m: int, n: int) -> int:
        if m <= 1 or n <= 1:
            return 1

        dp_table = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        dp_table[0][1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp_table[i][j] = dp_table[i - 1][j] + dp_table[i][j - 1]
        return dp_table[-1][-1]


# s = Solution()
# print(s.uniquePaths(3, 7))
# print(s.uniquePaths(3, 2))

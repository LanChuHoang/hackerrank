# https://leetcode.com/problems/distinct-subsequences/description/


class Solution:
    def numDistinct_v1(self, s: str, t: str) -> int:
        # num_sols(i, j) = num_sols(i + 1, j + 1) + num_sols(i + 1, j) if s[i] == s[j]
        # else num_sols(i + 1, j)
        # num_sols(i , j) = 1 if j >= len(t)
        # num_sols(i, j) = 0 if i >= len(s) but j < len(t) or len(s) - i < len(t) - j

        n, m = len(s), len(t)
        memo = [[-1 for _ in range(m)] for _ in range(n)]

        def num_sols(i: int, j: int):
            if j >= m:
                return 1

            if i >= n or n - i < m - j:
                return 0

            if memo[i][j] != -1:
                return memo[i][j]

            memo[i][j] = num_sols(i + 1, j)
            if s[i] == t[j]:
                memo[i][j] += num_sols(i + 1, j + 1)

            return memo[i][j]

        return num_sols(0, 0)

    def numDistinct(self, s: str, t: str) -> int:
        # go bottom-up from nums(n-1, m-1) to nums(0, 0)
        # nums(i, j) = nums(i + 1, j) + nums(i + 1, j + 1) if s[i] == t[j] else
        # nums(i + 1, j)

        n, m = len(s), len(t)
        dp_table = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            dp_table[i][-1] = 1
        for i in reversed(range(n)):
            for j in reversed(range(m)):
                dp_table[i][j] = dp_table[i + 1][j]
                if s[i] == t[j]:
                    dp_table[i][j] += dp_table[i + 1][j + 1]
        return dp_table[0][0]


# s = Solution()

# print(s.numDistinct(s="rabbbit", t="rabbit"))
# print(s.numDistinct(s="babgbag", t="bag"))

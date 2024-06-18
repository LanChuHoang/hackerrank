# https://leetcode.com/problems/regular-expression-matching/


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = dict()

        def dfs(i: int, j: int):
            if i >= len(s) and j >= len(p):
                return True

            if j >= len(p):
                return False

            if (i, j) in memo:
                return memo[(i, j)]

            result = False
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if j + 1 < len(p) and p[j + 1] == "*":
                result = dfs(i, j + 2) or (match and dfs(i + 1, j))
            elif match:
                result = dfs(i + 1, j + 1)

            memo[(i, j)] = result
            return result

        return dfs(0, 0)

# https://leetcode.com/problems/decode-ways/


class Solution:
    def numDecodings_v1(self, s: str) -> int:
        n = len(s)
        memo = [-1 for _ in range(n)]

        def dfs(i: int):
            if i > n or (i < n and s[i] == "0"):
                return 0
            if i == n:
                return 1

            if memo[i] != -1:
                return memo[i]

            memo[i] = dfs(i + 1)
            if i + 1 < n and int(s[i : i + 2]) <= 26:
                memo[i] += dfs(i + 2)
            return memo[i]

        return dfs(0)

    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = [0 for _ in range(n)]
        memo.extend([1, 0])

        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                continue
            memo[i] = memo[i + 1]
            if i + 1 < n and int(s[i : i + 2]) <= 26:
                memo[i] += memo[i + 2]

        return memo[0]


# s = Solution()
# print(s.numDecodings("27"))
# print(s.numDecodings("12"))
# print(s.numDecodings("226"))
# print(s.numDecodings("06"))

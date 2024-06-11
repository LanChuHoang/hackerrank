# https://leetcode.com/problems/longest-common-subsequence/description/


class Solution:
    def longestCommonSubsequence_v1(self, text1: str, text2: str) -> int:
        # For every i, j in text1 and text2
        # lcs(i, j) = lcs(i + 1, j + 1) + 1 if text1[i] == text2[j]
        # else = max(lcs(i + 1, j), lcs(i, j + 1))

        memo = dict()

        def lcs(i: int, j: int):
            if i >= len(text1) or j >= len(text2):
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            memo[(i, j)] = (
                1 + lcs(i + 1, j + 1)
                if text1[i] == text2[j]
                else max(lcs(i + 1, j), lcs(i, j + 1))
            )

            return memo[(i, j)]

        return lcs(0, 0)

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp_table = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        for i in reversed(range(len(text1))):
            for j in reversed(range(len(text2))):
                if text1[i] == text2[j]:
                    dp_table[i][j] = dp_table[i + 1][j + 1] + 1
                else:
                    dp_table[i][j] = max(dp_table[i + 1][j], dp_table[i][j + 1])
        return dp_table[0][0]

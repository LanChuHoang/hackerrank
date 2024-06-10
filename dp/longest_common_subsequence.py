# https://leetcode.com/problems/longest-common-subsequence/description/


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp_table = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        for i in reversed(range(len(text1))):
            for j in reversed(range(len(text2))):
                if text1[i] == text2[j]:
                    dp_table[i][j] = dp_table[i + 1][j + 1] + 1
                else:
                    dp_table[i][j] = max(dp_table[i + 1][j], dp_table[i][j + 1])
        return dp_table[0][0]

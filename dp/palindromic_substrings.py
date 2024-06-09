# https://leetcode.com/problems/palindromic-substrings/
import math


class Solution:
    def countSubstrings_v1(self, s: str) -> int:
        s = "@" + "#" + "#".join(s) + "#" + "$"
        total = 0
        for i in range(1, len(s) - 1):
            j = 0
            while s[i - (j + 1)] == s[i + (j + 1)]:
                j += 1
            if j != 0:
                total += math.ceil(j / 2)
        return total

    def countSubstrings(self, s: str) -> int:
        s = "@" + "#" + "#".join(s) + "#" + "$"
        total = 0
        dp_table = [0 for _ in range(len(s))]
        center, right = 0, 0
        for i in range(1, len(s) - 1):
            if i < right:
                mirr = 2 * center - i
                dp_table[i] = min(right - i, dp_table[mirr])

            while s[i - (dp_table[i] + 1)] == s[i + (dp_table[i] + 1)]:
                dp_table[i] += 1

            if dp_table[i] + i > right:
                center = i
                right = dp_table[i] + i

            if dp_table[i] != 0:
                total += math.ceil(dp_table[i] / 2)
        return total


# solution = Solution()
# print(solution.countSubstrings("aaa"))

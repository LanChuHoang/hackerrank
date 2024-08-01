# https://leetcode.com/problems/palindromic-substrings/


class Solution:
    def countSubstrings_v1(self, s: str) -> int:
        res = 0

        s = "@" + "#" + "#".join(s) + "#" + "$"
        n = len(s)

        for i in range(2, n - 2):
            j = 1
            while s[i - j] == s[i + j]:
                j += 1
            pan_len = j - 1
            num_pans = 0
            if pan_len and pan_len % 2 == 0:
                num_pans = pan_len // 2
            elif pan_len:
                num_pans = pan_len // 2 + 1
            res += num_pans
        return res

    def countSubstrings(self, s: str) -> int:
        s = "@" + "#" + "#".join(s) + "#" + "$"
        n = len(s)
        dp = [0 for _ in range(n)]
        center, right = 0, 0
        for i in range(2, n - 2):
            if i < right:
                mirr = 2 * center - i
                dp[i] = min(right - i, dp[mirr])
            while s[i - (dp[i] + 1)] == s[i + (dp[i] + 1)]:
                dp[i] += 1
            if i + dp[i] > right:
                center = i
                right = i + dp[i]

        res = 0
        for i in range(2, n - 2):
            res += dp[i] // 2
            if dp[i] % 2 != 0:
                res += 1
        return res


s = Solution()
print(s.countSubstrings(s="abc"))
print(s.countSubstrings(s="aaa"))

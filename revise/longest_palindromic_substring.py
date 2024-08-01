# https://leetcode.com/problems/longest-palindromic-substring/description/


class Solution:
    def longestPalindrome_v1(self, s: str) -> str:
        s = "@" + "#" + "#".join(s) + "#" + "$"
        n = len(s)

        res_len = 1
        res_i = 2
        for i in range(2, n - 2):
            j = 1
            while s[i - j] == s[i + j]:
                j += 1
            palindrom_len = j - 1
            if palindrom_len > res_len:
                res_len = palindrom_len
                res_i = i
        res = ""
        for i in range(res_i - res_len, res_i + res_len + 1):
            if s[i] != "#":
                res += s[i]
        return res

    def longestPalindrome(self, s: str) -> str:
        # Idea: maintain the nearest palindrome
        # so for each i
        # - If i is in the current palindrome -> we can use the precalculated length
        # from the left side to expand without going from scratch
        # -> len(i) = min(len(mirr), right - i)
        # because
        #   + if mirr pal inside main pal -> len(i) at least = len(mirr)
        #   + else if mirr pal beyonds main pal -> len(i) at least = abs(left - mirr) = right - i
        # -> then we continue to expand
        # - Else: there is no precalculated left part to use -> just expand from scratch
        # --> If pal at i goes beyond the main pal -> set i pal as the next main pal

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

        res_i, res_len = 0, 0
        for i in range(2, n - 2):
            if dp[i] > res_len:
                res_i, res_len = i, dp[i]

        res = ""
        for i in range(res_i - res_len, res_i + res_len + 1):
            if s[i] != "#":
                res += s[i]
        return res


# s = Solution()
# print(s.longestPalindrome("ABBA"))
# print(s.longestPalindrome("babad"))
# print(s.longestPalindrome("cbbd"))

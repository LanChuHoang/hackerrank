# https://leetcode.com/problems/longest-palindromic-substring/description/


class Solution:
    def longestPalindrome(self, s: str) -> str:
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


s = Solution()
print(s.longestPalindrome("ABBA"))
print(s.longestPalindrome("babad"))
print(s.longestPalindrome("cbbd"))

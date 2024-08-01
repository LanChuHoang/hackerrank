# https://leetcode.com/problems/palindromic-substrings/


class Solution:
    def countSubstrings(self, s: str) -> int:
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


s = Solution()
print(s.countSubstrings(s="abc"))
print(s.countSubstrings(s="aaa"))

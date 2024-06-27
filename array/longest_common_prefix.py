# https://leetcode.com/problems/longest-common-prefix/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def longestCommonPrefix_v1(self, strs: list[str]) -> str:
        result = []

        for i in range(len(strs[0])):
            cur_char = strs[0][i]
            for s in strs:
                if i >= len(s) or cur_char != s[i]:
                    return "".join(result)

            result.append(cur_char)

        return "".join(result)

    def longestCommonPrefix(self, strs: list[str]) -> str:
        min_s, max_s = min(strs), max(strs)

        for i in range(len(min_s)):
            if min_s[i] != max_s[i]:
                return min_s[:i]

        return min_s

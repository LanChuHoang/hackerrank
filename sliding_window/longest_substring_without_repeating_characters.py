# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        char_dict = dict()
        start = 0
        res = 0

        for i in range(len(s)):
            # print(start, i, s[i])
            if s[i] in char_dict and char_dict[s[i]] >= start:
                # print(start, i, s[i], "update", char_dict[s[i]], res, i - start)
                res = max(res, i - start)
                start = char_dict[s[i]] + 1

            char_dict[s[i]] = i

        res = max(res, len(s) - start)
        return res


# print(Solution().lengthOfLongestSubstring("abcbde"))

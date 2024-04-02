# https://leetcode.com/problems/longest-repeating-character-replacement/


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, end = 0, 0
        res = 0

        frequency = dict()
        frequency[s[end]] = 1
        while end < len(s) and start < len(s):
            window_len = end - start + 1
            max_frequency = max(frequency.values())
            num_changes = window_len - max_frequency
            # print(start, end, window_len, max_frequency, num_changes, frequency)

            if num_changes <= k:
                res = max(res, window_len)
                end += 1
                if end < len(s):
                    frequency[s[end]] = frequency.get(s[end], 0) + 1
            else:
                frequency[s[start]] -= 1
                start += 1

        return res


# print(Solution().characterReplacement(s="AABABBA", k=1))

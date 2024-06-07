# https://leetcode.com/problems/longest-palindromic-substring/description/


class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = "@" + "#" + "#".join(s) + "#" + "$"
        dp_table = [0 for _ in range(len(s))]
        center, right = 0, 0

        for i in range(1, len(s) - 1):
            # Try to update the pre calculated length to the current i
            if i < right:
                mirr = 2 * center - i
                dp_table[i] = min(right - i, dp_table[mirr])

            # Expand the current center i using the precalculated result if it exists
            while s[i + (1 + dp_table[i])] == s[i - (1 + dp_table[i])]:
                dp_table[i] += 1

            # Move the main center to the current i if the length of the current palindrom
            # exceeds the right boundary

            if i + dp_table[i] > right:
                center = i
                right = i + dp_table[i]

        max_length, max_center_idx = dp_table[1], 1
        for i in range(1, len(s) - 1):
            if dp_table[i] > max_length:
                max_length = dp_table[i]
                max_center_idx = i

        result = []
        left_idx = max_center_idx - max_length
        right_idx = max_center_idx + max_length
        for i in range(left_idx, right_idx + 1):
            if s[i] != "#":
                result.append(s[i])
        result = "".join(result)
        return result


# print(Solution().longestPalindrome("ABBA"))

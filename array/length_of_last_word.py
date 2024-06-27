# https://leetcode.com/problems/length-of-last-word/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        first_char_idx = None

        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                if first_char_idx is not None:
                    return first_char_idx - i
            else:
                if first_char_idx is None:
                    first_char_idx = i

        return 0 if first_char_idx is None else first_char_idx

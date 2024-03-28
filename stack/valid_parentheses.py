# https://leetcode.com/problems/valid-parentheses/
from collections import deque


class Solution:
    def isCloseParentheses(self, c: str) -> bool:
        return c == ")" or c == "]" or c == "}"

    def isValid(self, s: str) -> bool:
        info = {
            "(": (True, ")"),
            "[": (True, "]"),
            "{": (True, "}"),
            ")": (False, "("),
            "]": (False, "["),
            "}": (False, "{"),
        }
        stack = deque()
        for c in s:
            is_open, expected_close = info[c]
            if is_open:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                top_el = stack.pop()
                if top_el != expected_close:
                    return False
        return len(stack) == 0

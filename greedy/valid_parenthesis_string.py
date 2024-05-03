# https://leetcode.com/problems/valid-parenthesis-string/description/

from collections import deque


class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = deque()

        for c in s:
            if c == "(":
                stack.append(c)
            elif c == ")":
                if not stack or stack[-1] != "(":
                    return False
                stack.pop()

        return not stack


print(Solution().checkValidString("(()())"))
print(Solution().checkValidString("(())"))
print(Solution().checkValidString("(()"))
print(Solution().checkValidString("))()"))

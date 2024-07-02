# https://leetcode.com/problems/simplify-path/?envType=study-plan-v2&envId=top-interview-150

from collections import deque


# Idea: using stack to store the hierachy of the folder, if the operator is ".." -> move out by popping stack


class Solution:
    def simplifyPath(self, path: str) -> str:
        # path = path.replace("//", "")
        ops = path.split("/")
        stack = deque()
        for op in ops:
            if not op or op == ".":
                continue
            if op == ".." and stack:
                stack.pop()
            elif op != "..":
                stack.append(op)

        result = "/" + "/".join(stack)
        return result

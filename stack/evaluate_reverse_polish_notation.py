# https://leetcode.com/problems/evaluate-reverse-polish-notation/

from collections import deque


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = deque()

        for token in tokens:
            if token == "+":
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(operand1 + operand2)
            elif token == "-":
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(operand1 - operand2)
            elif token == "*":
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(operand1 * operand2)
            elif token == "/":
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(int(operand1 / operand2))
            else:
                stack.append(int(token))

        return stack.pop()

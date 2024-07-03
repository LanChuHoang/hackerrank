# https://leetcode.com/problems/basic-calculator/description/?envType=study-plan-v2&envId=top-interview-150

from collections import deque


class Solution:
    # def do_op(self, a: int, b: int, op: str):
    #     if op == "+":
    #         result = a + b
    #     elif op == "-":
    #         result = a - b
    #     else:
    #         raise ValueError(f"Invalid op {op}")
    #     return result

    # def calculate_v1(self, s: str) -> int:
    #     s = (
    #         s.replace(" ", "")
    #         .replace("(-", "(0-")
    #         .replace(")", " ) ")
    #         .replace("(", " ( ")
    #         .replace("+", " + ")
    #         .replace("-", " - ")
    #         .split()
    #     )

    #     operand_stack = deque()
    #     operator_stack = deque()

    #     if s[0] == "-":
    #         operand_stack.append(0)

    #     for c in s:
    #         if c != "(" and c != "+" and c != "-" and c != ")":
    #             operand_stack.append(int(c))
    #         elif c == "(":
    #             operator_stack.append(c)
    #         else:
    #             while operator_stack and operator_stack[-1] != "(":
    #                 op = operator_stack.pop()
    #                 second_operand = operand_stack.pop()
    #                 first_operand = operand_stack.pop()
    #                 result = self.do_op(first_operand, second_operand, op)
    #                 operand_stack.append(result)
    #             if c != ")":
    #                 operator_stack.append(c)
    #             else:
    #                 operator_stack.pop()

    #     while operator_stack:
    #         op = operator_stack.pop()
    #         second_operand = operand_stack.pop()
    #         first_operand = operand_stack.pop()
    #         result = self.do_op(first_operand, second_operand, op)
    #         operand_stack.append(result)

    #     return operand_stack[0]

    def calculate(self, s: str) -> int:
        # Insight 1: Because the expression only contains + and - (same precedence)
        # -> only store a cur_res (result so far), sign, and the current number
        # every time we meet a operator, do the calculation
        # current result = current result + sign * current number
        # and store the new sign and reset current number for later calculations
        # -> dont need to store the operator stack because there always has 1 operator at a time

        # Insight 2: For handling brackets
        # - For "(":
        #   + Store the current result and current sign in a stack, so that when we meet ")", we can combine
        # later when we meet ")", by current result = current result (previous stored in stack)
        # + sign (previous stored in stack) * current result (result of the expression inside brackets)
        #   + We need stack to handle nested brackets like a + (b + (c + d))
        #   + Note: we need to reset the current result to 0, and sign to 1 for inside bracket calculations
        # - For ")":
        #   + Do the combination as the above

        stack = deque()
        cur_res = 0
        cur_number = 0
        sign = 1

        for c in s:
            if c.isdigit():
                cur_number = cur_number * 10 + int(c)
            elif c == "+":
                cur_res += cur_number * sign
                cur_number = 0
                sign = 1
            elif c == "-":
                cur_res += cur_number * sign
                cur_number = 0
                sign = -1
            elif c == "(":
                stack.append(cur_res)
                stack.append(sign)
                cur_res = 0
                sign = 1
            elif c == ")":
                cur_res += cur_number * sign
                cur_res *= stack.pop()
                cur_res += stack.pop()
                cur_number = 0
            else:
                pass

        cur_res += cur_number * sign
        return cur_res


# s = Solution()
# print(s.calculate("1"))
# print(s.calculate("(1+(4+5+2)-3)+(6+8)"))
# print(s.calculate("1-(     -2)"))

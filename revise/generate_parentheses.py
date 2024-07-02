# https://leetcode.com/problems/generate-parentheses/


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        cur_combination = []

        def backtrack(num_opens: int, num_closes: int):
            if num_opens == num_closes == n:
                result.append("".join(cur_combination))
                return

            if num_closes < num_opens:
                cur_combination.append(")")
                backtrack(num_opens, num_closes + 1)
                cur_combination.pop()
            if num_opens < n:
                cur_combination.append("(")
                backtrack(num_opens + 1, num_closes)
                cur_combination.pop()

        backtrack(0, 0)
        return result

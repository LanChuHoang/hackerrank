# https://leetcode.com/problems/letter-combinations-of-a-phone-number/


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        result = []
        combination = []
        digit_letter_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def dfs(i: int):
            nonlocal result, combination
            if i == len(digits):
                if combination:
                    result.append("".join(combination))
                return

            for char in digit_letter_map.get(digits[i]):
                combination.append(char)
                dfs(i + 1)
                combination.pop()

        dfs(0)
        return result


print(Solution().letterCombinations("7"))

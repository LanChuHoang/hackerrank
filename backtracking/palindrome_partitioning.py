# https://leetcode.com/problems/palindrome-partitioning/


class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result = []
        cur_partition = []

        def is_palindrome(word: list[str]) -> bool:
            if len(word) < 2:
                return True

            for i in range(len(word) // 2):
                if word[i] != word[len(word) - 1 - i]:
                    return False

            return True

        def dfs(i: int, sub_s: list[str]):
            nonlocal result, cur_partition

            if i == len(s):
                if is_palindrome(sub_s):
                    cur_partition.append("".join(sub_s))
                    result.append(cur_partition.copy())
                    cur_partition.pop()
                return

            # go left, not split at i (between i and i + 1)
            sub_s.append(s[i])
            dfs(i + 1, sub_s)
            sub_s.pop()

            # go right, split at i
            if sub_s and is_palindrome(sub_s):
                cur_partition.append("".join(sub_s))
                dfs(i + 1, [s[i]])
                cur_partition.pop()

        dfs(0, [])

        return result


# print(Solution().partition("a"))

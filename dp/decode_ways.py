# https://leetcode.com/problems/decode-ways/description/

from collections import defaultdict


class Solution:
    def numDecodings_v1(self, s: str) -> int:
        result = 0

        def backtrack(i: int):
            nonlocal result

            if i >= len(s):
                result += 1
                return

            if s[i] == "0":
                return

            # split at this position - move 1
            backtrack(i + 1)

            # split at i + 1 - move 2
            if i + 1 >= len(s) or (s[i] == "2" and int(s[i + 1]) > 6) or int(s[i]) > 2:
                return

            backtrack(i + 2)

        backtrack(0)
        return result

    def numDecodings_v2(self, s: str) -> int:
        cache = defaultdict(int)

        def backtrack(i: int):
            if i >= len(s):
                return 1

            if s[i] == "0":
                return 0

            if cache[i]:
                return cache[i]

            local_num_ways = 0
            # split at this position - move 1
            local_num_ways += backtrack(i + 1)
            cache[i] = local_num_ways

            # split at i + 1 - move 2
            if i + 1 >= len(s) or (s[i] == "2" and int(s[i + 1]) > 6) or int(s[i]) > 2:
                return local_num_ways

            local_num_ways += backtrack(i + 2)
            cache[i] = local_num_ways
            return local_num_ways

        backtrack(0)
        return cache[0]

    def numDecodings(self, s: str) -> int:
        dp_table = [0 for _ in range(len(s) + 2)]
        dp_table[-1] = 1
        dp_table[-2] = 1
        s += "##"
        for i in reversed(range(len(s) - 2)):
            if s[i] == "0":
                continue

            # split 1 + dp_table[i + 1]
            dp_table[i] += dp_table[i + 1]

            # split 2 + dp_table[i + 2]
            if s[i + 1] == "#" or int(s[i] + s[i + 1]) < 1 or int(s[i] + s[i + 1]) > 26:
                continue
            dp_table[i] += dp_table[i + 2]

        return dp_table[0]


# solution = Solution()
# print(solution.numDecodings("11106"))
# print(solution.numDecodings("226"))
# print(solution.numDecodings("06"))

# https://leetcode.com/problems/interleaving-string/


class Solution:
    def isInterleave_v1(self, s1: str, s2: str, s3: str) -> bool:
        memo = dict()

        def dfs(i: int, j: int, k: int):
            if k >= len(s3):
                return i >= len(s1) and j >= len(s2)

            if (i, j, k) in memo:
                return memo[(i, j, k)]
            is_s1 = dfs(i + 1, j, k + 1) if i < len(s1) and s3[k] == s1[i] else False
            is_s2 = dfs(i, j + 1, k + 1) if j < len(s2) and s3[k] == s2[j] else False
            memo[(i, j, k)] = is_s1 or is_s2
            return memo[(i, j, k)]

        return dfs(0, 0, 0)

    def isInterleave_v2(self, s1: str, s2: str, s3: str) -> bool:
        # Optimization: k is calculated using i, j -> i = 0, j = 1 or i = 1, j = 0, k = 1
        # dfs(0, 1) and dfs(1, 0) and use the same cached result -> time comlexity reduced to O(n * m)
        # Op2: only calculate is_s2 if is_s1 is False
        memo = dict()

        def dfs(i: int, j: int):
            k = i + j
            if k >= len(s3):
                return i >= len(s1) and j >= len(s2)

            if (i, j) in memo:
                return memo[(i, j)]
            is_s1 = dfs(i + 1, j) if i < len(s1) and s3[k] == s1[i] else False
            is_s2 = (
                dfs(i, j + 1)
                if is_s1 is False and j < len(s2) and s3[k] == s2[j]
                else False
            )
            memo[(i, j)] = is_s1 or is_s2
            return memo[(i, j)]

        return dfs(0, 0)

    def isInterleave_v3(self, s1: str, s2: str, s3: str) -> bool:
        # Optimization 2: go bottom-up from (len(s1), len(s2)) -> (0, 0)
        # Reduce the running time because no need to create functions and stacks
        # for recursive calls
        if len(s3) != len(s1) + len(s2):
            return False

        s1 += "1"
        s2 += "2"
        s3 += "1"
        dp_table = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        dp_table[-1][-2] = True

        for i in reversed(range(len(s1))):
            for j in reversed(range(len(s2))):
                k = i + j
                is_s1 = dp_table[i + 1][j] if s1[i] == s3[k] else False
                is_s2 = dp_table[i][j + 1] if s2[j] == s3[k] else False
                dp_table[i][j] = is_s1 or is_s2

        return dp_table[0][0]

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Optimization 3: only store the last row -> reduced space to O(s2.length) and recuded running time
        # because we dont have to init n*m matrix
        if len(s3) != len(s1) + len(s2):
            return False

        s1 += "1"
        s2 += "2"
        s3 += "1"
        dp_table = [False for _ in range(len(s2) + 1)]
        dp_table[-2] = True

        for i in reversed(range(len(s1))):
            for j in reversed(range(len(s2))):
                k = i + j
                is_s1 = dp_table[j] if s1[i] == s3[k] else False
                is_s2 = dp_table[j + 1] if s2[j] == s3[k] else False
                dp_table[j] = is_s1 or is_s2

        return dp_table[0]


# s = Solution()
# print(s.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac"))
# print(s.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc"))
# print(s.isInterleave(s1="a", s2="b", s3="a"))
# print(s.isInterleave(s1="aac", s2="abd", s3="aaacbd"))

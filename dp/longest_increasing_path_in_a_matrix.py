# https://neetcode.io/roadmap


class Solution:
    def longestIncreasingPath_v1(self, matrix: list[list[int]]) -> int:
        result = 0
        m, n = len(matrix), len(matrix[0])
        visited = set()

        def dfs(i: int, j: int):
            visited.add((i, j))
            max_len = 0
            shifts = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for shift_i, shift_j in shifts:
                next_i, next_j = i + shift_i, j + shift_j
                if (
                    0 <= next_i < m
                    and 0 <= next_j < n
                    and matrix[i][j] < matrix[next_i][next_j]
                    and (next_i, next_j) not in visited
                ):
                    max_len = max(max_len, dfs(next_i, next_j))

            visited.remove((i, j))
            return max_len + 1

        for i in range(m):
            for j in range(n):
                result = max(result, dfs(i, j))

        return result

    def longestIncreasingPath_v2(self, matrix: list[list[int]]) -> int:
        # Optimization 1: lip(i, j) = lip(i', j') + 1 if matrix[i][j] < matrix[i'][j']
        # because the path the i', j' took is always different that the path that i, j took
        # so every path that lead to i', j' can use its result without checking again
        # -> Caching results
        # We also eliminate the visited set, because the new node never be the previous node
        # since the path we follow is strictly increasing

        result = 0
        m, n = len(matrix), len(matrix[0])
        memo = [[0 for _ in range(n)] for _ in range(m)]

        def dfs(i: int, j: int):
            if memo[i][j]:
                return memo[i][j]

            max_len = 0
            shifts = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for shift_i, shift_j in shifts:
                next_i, next_j = i + shift_i, j + shift_j
                if (
                    0 <= next_i < m
                    and 0 <= next_j < n
                    and matrix[i][j] < matrix[next_i][next_j]
                ):
                    max_len = max(max_len, dfs(next_i, next_j))

            memo[i][j] = max_len + 1
            return memo[i][j]

        for i in range(m):
            for j in range(n):
                result = max(result, dfs(i, j))

        return result

    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        # Optimization 3: go bottom-up from the largest element to the smallest

        result = 0
        m, n = len(matrix), len(matrix[0])
        dp_table = [[0 for _ in range(n)] for _ in range(m)]
        positions = dict()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] not in positions:
                    positions[matrix[i][j]] = [(i, j)]
                else:
                    positions[matrix[i][j]].append((i, j))

        for key in reversed(sorted(positions.keys())):
            for i, j in positions[key]:
                max_len = 0
                shifts = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                for shift_i, shift_j in shifts:
                    next_i, next_j = i + shift_i, j + shift_j
                    if (
                        0 <= next_i < m
                        and 0 <= next_j < n
                        and matrix[i][j] < matrix[next_i][next_j]
                    ):
                        max_len = max(max_len, dp_table[next_i][next_j])
                dp_table[i][j] = max_len + 1
                result = max(result, dp_table[i][j])

        return result


# s = Solution()
# print(s.longestIncreasingPath(matrix=[[9, 9, 4], [6, 6, 8], [2, 1, 1]]))
# print(s.longestIncreasingPath(matrix=[[3, 4, 5], [3, 2, 6], [2, 2, 1]]))
# print(s.longestIncreasingPath(matrix=[[1]]))
# print(
#     s.longestIncreasingPath(
#         matrix=[[0, 9, 7, 0], [7, 4, 1, 9], [2, 6, 1, 3], [8, 0, 9, 9]]
#     )
# )

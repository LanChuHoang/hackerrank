# https://leetcode.com/problems/magic-squares-in-grid/description/


class Solution:
    def is_magic(
        self, grid: list[list[int]], rows: int, cols: int, start_i: int, start_j: int
    ):
        visited = [False for _ in range(9)]
        sum_rows = [0, 0, 0]
        sum_cols = [0, 0, 0]
        for i in range(start_i, start_i + 3):
            for j in range(start_j, start_j + 3):
                if (
                    i >= rows
                    or j >= rows
                    or grid[i][j] > 9
                    or grid[i][j] < 1
                    or visited[grid[i][j] - 1]
                ):
                    return False

                r, c = i - start_i, j - start_j
                sum_rows[r] += grid[i][j]
                sum_cols[c] += grid[i][j]
                visited[grid[i][j] - 1] = True

        for sum_row in sum_rows:
            if sum_row != sum_rows[0]:
                return False
        for sum_col in sum_cols:
            if sum_col != sum_rows[0]:
                return False
        sum_d1, sum_d2 = 0, 0
        for k in range(3):
            d1_i, d1_j = start_i + k, start_j + k
            d2_i, d2_j = start_i + k, start_j + 2 - k
            if d1_i >= rows or d1_j >= cols or d2_i >= rows or d2_j >= cols:
                return False
            sum_d1 += grid[d1_i][d1_j]
            sum_d2 += grid[d2_i][d2_j]
        return sum_d1 == sum_rows[0] and sum_d2 == sum_rows[0]

    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        # loop through array -> for each i, j
        # check a square which has the corners as
        # (i, j), (i, j + 2), (i + 2, j + 2), (i + 2, j)

        rows, cols = len(grid), len(grid[0])
        res = 0
        for i in range(rows):
            for j in range(cols):
                if self.is_magic(grid, rows, cols, i, j):
                    res += 1

        return res


s = Solution()
print(s.numMagicSquaresInside(grid=[[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]))
print(s.numMagicSquaresInside(grid=[[8]]))
print(s.numMagicSquaresInside([[5, 5, 5], [5, 5, 5], [5, 5, 5]]))

class Solution:
    def flip_rows(self, grid: list[list[int]], m: int, n: int) -> int:
        res = 0
        for row in grid:
            for i in range(n // 2):
                j = n - 1 - i
                if row[i] != row[j]:
                    res += 1

        return res

    def flip_cols(self, grid: list[list[int]], m: int, n: int) -> int:
        res = 0
        for j in range(n):
            for i in range(m // 2):
                k = m - 1 - i
                if grid[i][j] != grid[k][j]:
                    res += 1

        return res

    def minFlips(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        return min(self.flip_rows(grid, m, n), self.flip_cols(grid, m, n))

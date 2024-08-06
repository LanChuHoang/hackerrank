class neighborSum:
    def __init__(self, grid: list[list[int]]):
        self.grid = grid
        self.idx_map = dict()
        self.n = len(grid)
        for i in range(self.n):
            for j in range(self.n):
                self.idx_map[grid[i][j]] = (i, j)

    def adjacentSum(self, value: int) -> int:
        i, j = self.idx_map[value]
        res = 0
        shifts = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for shift_i, shift_j in shifts:
            next_i = i + shift_i
            next_j = j + shift_j
            if 0 <= next_i < self.n and 0 <= next_j < self.n:
                res += self.grid[next_i][next_j]
        return res

    def diagonalSum(self, value: int) -> int:
        i, j = self.idx_map[value]
        res = 0
        shifts = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for shift_i, shift_j in shifts:
            next_i = i + shift_i
            next_j = j + shift_j
            if 0 <= next_i < self.n and 0 <= next_j < self.n:
                res += self.grid[next_i][next_j]
        return res


# Your neighborSum object will be instantiated and called as such:
s = neighborSum([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print(s.adjacentSum(1))
print(s.adjacentSum(4))
print(s.diagonalSum(4))
print(s.diagonalSum(8))

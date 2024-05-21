# competitive programming handbook
# find the path that have a maximumn sum in a grid. Only move bot or right
# must go from top left to bottom right


def brute_force(grid: list[list[int]]):
    max_so_far = 0
    cur_sum = 0

    def dfs(i: int, j: int):
        nonlocal max_so_far, cur_sum

        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid):
            return

        cur_sum += grid[i][j]
        if i == len(grid) - 1 and i == j:
            max_so_far = max(max_so_far, cur_sum)
        else:
            dfs(i + 1, j)
            dfs(i, j + 1)
        cur_sum -= grid[i][j]

    dfs(0, 0)
    return max_so_far


def top_down_memo(grid: list[list[int]]):
    cache = dict()

    def dfs(i: int, j: int):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid):
            return 0

        if (i, j) not in cache:
            local_max_sum = grid[i][j] + max(dfs(i + 1, j), dfs(i, j + 1))
            cache[(i, j)] = local_max_sum
        else:
            local_max_sum = cache[(i, j)]
        return local_max_sum

    return dfs(0, 0)


def bottom_up(grid: list[list[int]]):
    dp_table = [[0 for _ in range(len(grid) + 1)] for _ in range(len(grid) + 1)]
    for i in range(1, len(grid) + 1):
        for j in range(1, len(grid) + 1):
            dp_table[i][j] = (
                max(dp_table[i - 1][j], dp_table[i][j - 1]) + grid[i - 1][j - 1]
            )

    return dp_table[-1][-1]


if __name__ == "__main__":
    grid = [
        [1, 7, 8],
        [4, 2, 99],
        [5, 6, 3],
    ]
    print(bottom_up(grid))

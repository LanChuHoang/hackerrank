# https://leetcode.com/problems/n-queens/description/


class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        result = []

        board = [["." for _ in range(n)] for _ in range(n)]

        column_placed = [False for _ in range(n)]
        diag1_placed = [False for _ in range((n - 1) * 2 + 1)]
        diag2_placed = diag1_placed.copy()

        def dfs(i: int):
            nonlocal result, board, column_placed, diag1_placed
            if i == n:
                serialized_board = ["".join(row) for row in board]
                result.append(serialized_board)
                return

            for j in range(n):
                if (
                    not column_placed[j]
                    and not diag1_placed[i - j]
                    and not diag2_placed[n - 1 - i - j]
                ):
                    board[i][j] = "Q"
                    column_placed[j] = True
                    diag1_placed[i - j] = True
                    diag2_placed[n - 1 - i - j] = True
                    dfs(i + 1)
                    board[i][j] = "."
                    column_placed[j] = False
                    diag1_placed[i - j] = False
                    diag2_placed[n - 1 - i - j] = False

        dfs(0)

        return result


# print(Solution().solveNQueens(4))

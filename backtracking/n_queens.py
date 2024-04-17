# https://leetcode.com/problems/n-queens/description/


class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        result = []

        board = [["." for _ in range(n)] for _ in range(n)]

        column_placed = [False for _ in range(n)]
        diag_placed = [False for _ in range((n - 1) * 2 + 1)]

        def dfs(i: int):
            nonlocal result, board, column_placed, diag_placed
            if i == n:
                serialized_board = ["".join(row) for row in board]
                result.append(serialized_board)
                return

            for j in range(n):
                if not column_placed[j] and not diag_placed[i - j]:
                    board[i][j] = "Q"
                    column_placed[j] = True
                    diag_placed[i - j] = True
                    dfs(i + 1)
                    board[i][j] = "."
                    column_placed[j] = False
                    diag_placed[i - j] = False

        dfs(0)

        return result


print(Solution().solveNQueens(4))

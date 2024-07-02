# https://leetcode.com/problems/game-of-life/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        result = [[0 for _ in range(cols)] for _ in range(rows)]

        shifts = [(0, -1), (0, 1), (1, -1), (1, 0), (1, 1), (-1, -1), (-1, 0), (-1, 1)]
        for i in range(rows):
            for j in range(cols):
                num_lives = 0
                for shift_i, shift_j in shifts:
                    next_i, next_j = i + shift_i, j + shift_j
                    if (
                        0 <= next_i < rows
                        and 0 <= next_j < cols
                        and board[next_i][next_j] == 1
                    ):
                        num_lives += 1

                if (board[i][j] == 1 and 2 <= num_lives <= 3) or (
                    board[i][j] == 0 and num_lives == 3
                ):
                    result[i][j] = 1
        for i in range(rows):
            for j in range(cols):
                board[i][j] = result[i][j]

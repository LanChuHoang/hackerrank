# https://leetcode.com/problems/set-matrix-zeroes/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        z_rows = [0] * rows
        z_cols = [0] * cols

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    z_rows[i] = 1
                    z_cols[j] = 1

        for i in range(rows):
            for j in range(cols):
                if z_rows[i] or z_cols[j]:
                    matrix[i][j] = 0

# https://leetcode.com/problems/rotate-image/description/?envType=study-plan-v2&envId=top-interview-150

import math


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # transpose the matrix
        n = len(matrix)
        for i in range(n):
            for j in range(math.ceil(n / 2)):
                if i < j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                op_j = n - 1 - j
                if op_j != j:
                    if i < op_j:
                        matrix[i][op_j], matrix[op_j][i] = (
                            matrix[op_j][i],
                            matrix[i][op_j],
                        )
                    matrix[i][j], matrix[i][op_j] = matrix[i][op_j], matrix[i][j]


#         print(matrix)


# Solution().rotate(
#     matrix=[
#         [5, 1, 9, 11],
#         [2, 4, 8, 10],
#         [13, 3, 6, 7],
#         [15, 14, 12, 16],
#     ]
# )

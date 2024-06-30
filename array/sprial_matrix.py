# https://leetcode.com/problems/spiral-matrix/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []
        rows = len(matrix)
        columns = len(matrix[0])
        left, right, bottom, top = 0, columns - 1, rows - 1, 0
        while len(result) < rows * columns:
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        return result


# print(Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))

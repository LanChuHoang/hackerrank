# https://leetcode.com/problems/search-a-2d-matrix/description/


class Solution:
    def binary_search(
        self, matrix: list[list[int]], target: int, left: int, right: int
    ):
        if left > right:
            return False

        mid = (left + right) // 2
        # m = len(matrix)
        n = len(matrix[0])
        i = mid // n
        j = mid % n
        # print(left, right, mid, i, j, matrix[i][j], m, n)
        if matrix[i][j] == target:
            return True
        elif target > matrix[i][j]:
            return self.binary_search(matrix, target, mid + 1, right)
        else:
            return self.binary_search(matrix, target, left, mid - 1)

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        last_flat_index = n * (m - 1) + (n - 1)
        return self.binary_search(matrix, target, 0, last_flat_index)


# print(Solution().searchMatrix([[1, 3]], target=3))

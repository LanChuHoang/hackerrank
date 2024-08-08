# https://leetcode.com/problems/spiral-matrix-iii/description/


class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> list[list[int]]:
        res = [[rStart, cStart]]
        total_cells = rows * cols

        turn = 0
        i, j = rStart, cStart
        while len(res) < total_cells:
            # go right
            j += 1
            if 0 <= i < rows and 0 <= j < cols:
                res.append([i, j])

            # go down
            dest_i = i + 1 + turn * 2
            i += 1
            while i <= dest_i:
                if 0 <= i < rows and 0 <= j < cols:
                    res.append([i, j])
                i += 1
            i -= 1

            # go left
            dest_j = j - (2 + turn * 2)
            j -= 1
            while j >= dest_j:
                if 0 <= i < rows and 0 <= j < cols:
                    res.append([i, j])
                j -= 1
            j += 1

            # go up
            dest_i = i - (2 + turn * 2)
            i -= 1
            while i >= dest_i:
                if 0 <= i < rows and 0 <= j < cols:
                    res.append([i, j])
                i -= 1
            i += 1

            # go right
            dest_j = j + 2 + turn * 2
            j += 1
            while j <= dest_j:
                if 0 <= i < rows and 0 <= j < cols:
                    res.append([i, j])
                j += 1
            j -= 1

            # next turn
            turn += 1

        return res


# s = Solution()
# print(s.spiralMatrixIII(rows=1, cols=4, rStart=0, cStart=0))
# print(s.spiralMatrixIII(rows=5, cols=6, rStart=1, cStart=4))

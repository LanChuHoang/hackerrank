# https://leetcode.com/problems/valid-sudoku/


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        index_sets = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    row_index = f"{board[i][j]}r{i}"
                    if row_index in index_sets:
                        return False
                    index_sets.add(row_index)

                    col_index = f"{board[i][j]}c{j}"
                    if col_index in index_sets:
                        return False
                    index_sets.add(col_index)

                    block_index = f"{board[i][j]}b{i//3}{j//3}"
                    if block_index in index_sets:
                        return False
                    index_sets.add(block_index)
        return True

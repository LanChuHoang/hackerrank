# https://leetcode.com/problems/word-search/description/


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        visited = set()

        def search(board_i: int, board_j: int, word_i: int):
            nonlocal visited

            if board[board_i][board_j] != word[word_i]:
                return False

            if word_i == len(word) - 1:
                return True

            # search the next board position to move
            visited.add((board_i, board_j))
            next_word_i = word_i + 1
            # top, right, bot, left
            position_shifts = [
                (-1, 0),
                (0, 1),
                (1, 0),
                (0, -1),
            ]
            for shift_i, shift_j in position_shifts:
                next_i = board_i + shift_i
                next_j = board_j + shift_j
                if (
                    0 <= next_i < len(board)
                    and 0 <= next_j < len(board[0])
                    and (next_i, next_j) not in visited
                ):
                    exist = search(next_i, next_j, next_word_i)
                    if exist:
                        return True

            visited.remove((board_i, board_j))
            return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if search(i, j, 0):
                    return True
        return False

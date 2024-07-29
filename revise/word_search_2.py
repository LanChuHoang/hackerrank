# https://leetcode.com/problems/word-search-ii/description/


class Solution:
    def word_in_board(
        self,
        board: list[list[str]],
        board_x: int,
        board_y: int,
        word: str,
        word_i: int,
        visited: set,
    ):
        if word_i == len(word) - 1:
            return True

        visited.add((board_x, board_y))
        res = False
        shifts = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        for shift_x, shift_y in shifts:
            next_x, next_y = board_x + shift_x, board_y + shift_y
            next_i = word_i + 1
            if (
                0 <= next_x < len(board)
                and 0 <= next_y < len(board[0])
                and (next_x, next_y) not in visited
                and next_i < len(word)
                and board[next_x][next_y] == word[next_i]
                and self.word_in_board(board, next_x, next_y, word, next_i, visited)
            ):
                res = True
                break
        visited.remove((board_x, board_y))
        return res

    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        board_idxs = dict()
        for i in range(len(board)):
            for j in range(len(board[0])):
                c = board[i][j]
                if c in board_idxs:
                    board_idxs[c].append((i, j))
                else:
                    board_idxs[c] = [(i, j)]

        res = []
        for w in words:
            for i, j in board_idxs.get(w[0], []):
                if self.word_in_board(board, i, j, w, 0, set()):
                    res.append(w)
                    break
        return res


# s = Solution()
# print(
#     s.findWords(
#         board=[
#             ["o", "a", "a", "n"],
#             ["e", "t", "a", "e"],
#             ["i", "h", "k", "r"],
#             ["i", "f", "l", "v"],
#         ],
#         words=["oath", "pea", "eat", "rain"],
#     )
# )
# print(s.findWords(board=[["a", "b"], ["c", "d"]], words=["abcb"]))
# print(s.findWords(board=[["a"]], words=["a"]))

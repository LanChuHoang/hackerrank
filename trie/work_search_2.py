# https://leetcode.com/problems/word-search-ii/description

from collections import defaultdict
# from utils import pt


class TrieNode:
    def __init__(
        self,
        val: str | None = None,
        is_terminal: bool = False,
        child_nodes: defaultdict | None = None,
    ) -> None:
        self.val = val
        self.is_terminal = is_terminal
        self.child_nodes = child_nodes if child_nodes else defaultdict(lambda: None)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        if not word:
            return

        def _insert(node: TrieNode | None, index: int):
            if index >= len(word):
                return
            if node is None:
                node = TrieNode(val=word[index])
            if index == len(word) - 1:
                node.is_terminal = True
                return node
            node.child_nodes[word[index + 1]] = _insert(
                node.child_nodes[word[index + 1]], index + 1
            )
            return node

        self.root.child_nodes[word[0]] = _insert(self.root.child_nodes[word[0]], 0)


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        result = set()
        trie = Trie()
        for word in words:
            trie.insert(word)
        # pt(trie.root)

        start_pos_dict = defaultdict(list)
        for i in range(len(board)):
            for j in range(len(board[i])):
                start_pos_dict[board[i][j]].append((i, j))

        shifts = [(0, -1), (-1, 0), (1, 0), (0, 1)]
        cur_chars = []
        visited = set()

        def _dfs(node: TrieNode | None, board_i: int, board_j: int):
            nonlocal result, cur_chars, visited
            if not node or node.val != board[board_i][board_j]:
                return

            if node.is_terminal:
                result.add("".join(cur_chars))

            for shift_i, shift_j in shifts:
                next_i = board_i + shift_i
                next_j = board_j + shift_j
                if (
                    0 <= next_i < len(board)
                    and 0 <= next_j < len(board[0])
                    and (next_i, next_j) not in visited
                    and board[next_i][next_j] in node.child_nodes
                ):
                    child = node.child_nodes[board[next_i][next_j]]
                    cur_chars.append(child.val)
                    visited.add((next_i, next_j))
                    _dfs(child, next_i, next_j)
                    visited.remove((next_i, next_j))
                    cur_chars.pop()

        for child in trie.root.child_nodes.values():
            if not child:
                continue

            cur_chars.append(child.val)
            for start_i, start_j in start_pos_dict[child.val]:
                visited.add((start_i, start_j))
                _dfs(child, start_i, start_j)
                visited.remove((start_i, start_j))

            cur_chars.pop()

        return list(result)


# print(
#     Solution().findWords(
#         [
#             ["o", "a", "a", "n"],
#             ["e", "t", "a", "e"],
#             ["i", "h", "k", "r"],
#             ["i", "f", "l", "v"],
#         ],
#         ["oath", "pea", "eat", "rain"],
#     )
# )
# print(Solution().findWords(board=[["a", "b"], ["c", "d"]], words=["abcb"]))
# print(Solution().findWords([["a", "a"]], ["aaa"]))

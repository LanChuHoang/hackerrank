# https://leetcode.com/problems/implement-trie-prefix-tree/description/

from collections import defaultdict


class TrieNode:
    def __init__(
        self,
        val: str | None = None,
        is_terminal: bool = False,
    ) -> None:
        self.val = val
        self.is_terminal = is_terminal
        self.child_nodes = defaultdict(lambda: None)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur_node = self.root
        for c in word:
            if not cur_node.child_nodes[c]:
                cur_node.child_nodes[c] = TrieNode(c)
            cur_node = cur_node.child_nodes[c]
        cur_node.is_terminal = True

    def search(self, word: str) -> bool:
        cur_node = self.root
        for c in word:
            if not cur_node.child_nodes[c]:
                return False
            cur_node = cur_node.child_nodes[c]
        return cur_node.is_terminal

    def startsWith(self, prefix: str) -> bool:
        cur_node = self.root
        for c in prefix:
            if not cur_node.child_nodes[c]:
                return False
            cur_node = cur_node.child_nodes[c]
        return True

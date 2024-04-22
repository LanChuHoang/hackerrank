# https://leetcode.com/problems/implement-trie-prefix-tree/description/

from collections import defaultdict


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

    def search(self, word: str) -> bool:
        if not word:
            return False

        def _dfs(node: TrieNode | None, index: int):
            if (
                index >= len(word)
                or node is None
                or node.val != word[index]
                or (index == len(word) - 1 and not node.is_terminal)
            ):
                return False
            if index == len(word) - 1 and node.is_terminal:
                return True
            return _dfs(node.child_nodes[word[index + 1]], index + 1)

        return _dfs(self.root.child_nodes[word[0]], 0)

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return False

        def _dfs(node: TrieNode | None, index: int):
            if index >= len(prefix) or node is None or node.val != prefix[index]:
                return False
            if index == len(prefix) - 1:
                return True
            return _dfs(node.child_nodes[prefix[index + 1]], index + 1)

        return _dfs(self.root.child_nodes[prefix[0]], 0)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

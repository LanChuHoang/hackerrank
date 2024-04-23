from collections import defaultdict
from utils import pt


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
            if not node:
                return False

            if index == len(word) - 1:
                return node.is_terminal

            char = word[index + 1]
            if char == ".":
                for child in node.child_nodes.values():
                    if child:
                        contains = _dfs(child, index + 1)
                        if contains:
                            return True
                return False
            else:
                return _dfs(node.child_nodes[word[index + 1]], index + 1)

        return _dfs(self.root, -1)


class WordDictionary:
    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        return self.trie.search(word)


obj = WordDictionary()
obj.addWord("at")
obj.addWord("and")
obj.addWord("an")
obj.addWord("add")
pt(obj.trie.root)
print(obj.search("a"))
print(obj.search(".at"))

obj.addWord("bat")
pt(obj.trie.root)
print(obj.search(".at"))
print(obj.search("an."))
print(obj.search("a.d."))
print(obj.search("b."))
print(obj.search("a.d"))
print(obj.search("."))

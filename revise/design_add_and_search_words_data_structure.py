# https://leetcode.com/problems/design-add-and-search-words-data-structure/

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


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur_node = self.root
        for c in word:
            if not cur_node.child_nodes[c]:
                cur_node.child_nodes[c] = TrieNode(c)
            cur_node = cur_node.child_nodes[c]
        cur_node.is_terminal = True

    def search(self, word: str) -> bool:
        def exist(node: TrieNode | None, idx: int):
            if idx == len(word):
                return node.is_terminal

            c = word[idx]
            if c != ".":
                next_node = node.child_nodes[c]
                if not next_node:
                    return False
                return exist(next_node, idx + 1)
            else:
                for next_node in node.child_nodes.values():
                    if next_node and exist(next_node, idx + 1):
                        return True
                return False

        return exist(self.root, 0)


s = WordDictionary()
s.addWord("at")
s.addWord("and")
s.addWord("an")
s.addWord("add")
print(s.search("a"))
print(s.search(".at"))
s.addWord("bat")
print(s.search(".at"))
print(s.search("an."))
print(s.search("a.d."))
print(s.search("b."))
print(s.search("a.d"))
print(s.search("."))

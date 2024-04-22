from PrettyPrint import PrettyPrintTree
from collections import defaultdict


pt = PrettyPrintTree(
    lambda x: list(x.child_nodes.values()) if x else [],
    lambda x: f"{x.val}, {x.is_terminal}" if x else None,
)


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

    def remove(self, word: str) -> None:
        def _has_no_child(node: TrieNode):
            for value in node.child_nodes.values():
                if value:
                    return False
            return True

        def _del(node: TrieNode | None, index: int):
            if not node:
                return None

            if index == len(word) - 1:
                node.is_terminal = False
                if _has_no_child(node):
                    del node
                    node = None
                return node

            node.child_nodes[word[index + 1]] = _del(
                node.child_nodes[word[index + 1]], index + 1
            )
            if not node.is_terminal and _has_no_child(node):
                del node
                node = None
            return node

        self.root.child_nodes[word[0]] = _del(self.root.child_nodes[word[0]], 0)

    def insert_many(self, *words) -> None:
        for word in words:
            self.insert(word)

    def startsWith(self, prefix: str) -> list[str]:
        pass

    def print(self):
        pt(self.root)


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert_many("chu", "chi", "hoa")
obj
obj.print()
print(obj.search("ch"))
print(obj.search("chu"))
print(obj.startsWith("ch"))
print(obj.startsWith("chu"))
obj.remove("ch")
obj.print()
obj.remove("chi")
obj.print()
obj.remove("hoa")
obj.print()
obj.remove("lan")
obj.print()


# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

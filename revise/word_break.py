# https://leetcode.com/problems/word-break/description/


class TrieNode:
    def __init__(self, val: str = None, is_terminal: bool = False) -> None:
        self.val = val
        self.is_terminal = is_terminal
        self.children = dict()


class Trie:
    def __init__(self, words: list[str]) -> None:
        self.root = TrieNode()
        for word in words:
            self.add_word(word)

    def add_word(self, word: str):
        cur_node = self.root
        for c in word:
            next_node = cur_node.children.get(c)
            if not next_node:
                next_node = TrieNode(c)
                cur_node.children[c] = next_node
            cur_node = next_node
        cur_node.is_terminal = True

    def has_prefix(self, prefix: str):
        cur_node = self.root
        for c in prefix:
            next_node = cur_node.children.get(c)
            if not next_node:
                return False, False
            cur_node = next_node

        return True, cur_node.is_terminal


class Solution:
    def wordBreak_v1(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        memo = [-1 for _ in range(n)]
        words = set(wordDict)

        def dfs(i: int):
            if i >= n:
                return True

            if memo[i] != -1:
                return memo[i]

            memo[i] = False
            for j in range(i, n):
                if s[i : j + 1] in words and dfs(j + 1):
                    memo[i] = True
                    break
            return memo[i]

        return dfs(0)

    def wordBreak_v2(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        memo = [-1 for _ in range(n)]
        trie = Trie(wordDict)

        def dfs(i: int):
            if i >= n:
                return True

            if memo[i] != -1:
                return memo[i]

            memo[i] = False
            for j in range(i, n):
                is_prefix, is_word = trie.has_prefix(s[i : j + 1])
                if not is_prefix:
                    break
                if is_word and dfs(j + 1):
                    memo[i] = True
                    break
            return memo[i]

        return dfs(0)

    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        m = max([len(w) for w in wordDict])
        memo = [False for _ in range(n)]
        words = set(wordDict)
        memo.append(True)

        for i in range(n - 1, -1, -1):
            for j in range(i, i + m + 1):
                if s[i : j + 1] in words and memo[j + 1]:
                    memo[i] = True
                    break
        return memo[0]


s = Solution()
print(s.wordBreak(s="leetcode", wordDict=["leet", "code"]))
print(s.wordBreak(s="applepenapple", wordDict=["apple", "pen"]))
print(s.wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))

# https://leetcode.com/problems/edit-distance/description/


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # At every i, j
        # If word1[i] != word2[j], there 3 dicisions:
        #   - remove word1[i] -> num_ops(i, j) = num_ops(i + 1, j) + 1
        #   --> we can replace (hold the current position)
        #   - insert new word1[i] = word[j] -> num_ops(i, j) = num_ops(i + 1, j + 1) + 1
        #   --> or we can insert (shift 1 to right) and later delete
        #   - replace word1[i] with word2[j] -> num_ops(i, j) = num_ops(i+1, j+1) + 1 if
        #   --> or we can delete (shift 1 to left) and later insert
        # Else
        #   num_ops(i, j) = num_ops(i + 1, j + 1)
        # if i >= len(word1) or j >= len(word2): return len(word1) - i + len(word2) - j

        n, m = len(word1), len(word2)
        memo = [[-1 for _ in range(m)] for _ in range(n)]

        def num_ops(i: int, j: int):
            if i >= n or j >= m:
                return (n - i) + (m - j)

            if memo[i][j] != -1:
                return memo[i][j]

            if word1[i] == word2[j]:
                memo[i][j] = num_ops(i + 1, j + 1)
            else:
                chose_remove = num_ops(i + 1, j)
                chose_insert = num_ops(i, j + 1)
                chose_replace = num_ops(i + 1, j + 1)
                memo[i][j] = min(chose_remove, chose_insert, chose_replace) + 1

            return memo[i][j]

        return num_ops(0, 0)


# s = Solution()

# print(s.minDistance(word1="horse", word2="ros"))
# print(s.minDistance(word1="intention", word2="execution"))

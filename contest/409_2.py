from collections import defaultdict


class Solution:
    def shortestDistanceAfterQueries(
        self, n: int, queries: list[list[int]]
    ) -> list[int]:
        res = []
        paths = defaultdict(list)
        memo = [n - i - 1 for i in range(n)]

        for src, dest in queries:
            paths[src].append(dest)

            for i in range(src, -1, -1):
                for dest in paths[i]:
                    memo[i] = min(memo[i], memo[dest] + 1)
                memo[i] = min(memo[i], memo[i + 1] + 1)

            res.append(memo[0])

        return res

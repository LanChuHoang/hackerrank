# from sortedcontainers import SortedList
from typing import List
import bisect


class Solution:
    def eraseMiddleNodes(self, s, l, r):
        start = bisect.bisect_left(s, l)
        end = bisect.bisect_right(s, r)
        del s[start:end]

    def shortestDistanceAfterQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:
        s = [i for i in range(n)]
        ans = []
        for x, y in queries:
            self.eraseMiddleNodes(s, x + 1, y - 1)
            ans.append(len(s) - 1)
        return ans


s = Solution()
print(s.shortestDistanceAfterQueries(n=5, queries=[[2, 4], [0, 2], [0, 4]]))
print(s.shortestDistanceAfterQueries(n=4, queries=[[0, 3], [0, 2]]))

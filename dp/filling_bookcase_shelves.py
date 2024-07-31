# https://leetcode.com/problems/filling-bookcase-shelves/submissions/1339240337/


class Solution:
    def minHeightShelves_v1(self, books: list[list[int]], shelfWidth: int) -> int:
        res = float("inf")
        n = len(books)

        def dfs(total_height: int, cur_height: int, cur_width: int, i: int):
            nonlocal res

            if i == n:
                res = min(res, total_height + cur_height)
                return

            if total_height > res:
                return

            w, h = books[i]
            if cur_width + w <= shelfWidth:
                dfs(total_height, max(cur_height, h), cur_width + w, i + 1)
            dfs(total_height + cur_height, h, w, i + 1)

        w, h = books[0]
        dfs(0, h, w, 1)
        return res

    def minHeightShelves_v2(self, books: list[list[int]], shelfWidth: int) -> int:
        # Idea:
        # f(i, cur_w, cur_h) = min(
        #   f(i + 1, b_w, b_h) + cur_h,
        #   f(i + 1, cur_w + b_w, max(cur_h, b_h))
        # )
        # - 2 choices:
        # + include the book[i] in the current shelf
        # + create a new shelf

        n = len(books)
        memo = [[0 for _ in range(shelfWidth + 1)] for _ in range(n)]

        def dfs(i: int, cur_w: int, cur_h: int):
            if i == n:
                return cur_h

            if memo[i][cur_w]:
                return memo[i][cur_w]

            b_w, b_h = books[i]
            memo[i][cur_w] = dfs(i + 1, b_w, b_h) + cur_h
            if cur_w + b_w <= shelfWidth:
                memo[i][cur_w] = min(
                    memo[i][cur_w], dfs(i + 1, cur_w + b_w, max(cur_h, b_h))
                )
            return memo[i][cur_w]

        return dfs(1, books[0][0], books[0][1])

    def minHeightShelves_v3(self, books: list[list[int]], shelfWidth: int) -> int:
        # Idea:
        # same as above but the state of current shelf is stored in that function
        # each time we call a function recursively -> means we start a new shelf

        n = len(books)
        memo = [0 for _ in range(n)]

        def dfs(i: int):
            if i == n:
                return 0

            if memo[i]:
                return memo[i]

            remain_width = shelfWidth
            max_h = 0
            res = float("inf")
            for j in range(i, n):
                w, h = books[j]
                if remain_width < w:
                    break
                max_h = max(max_h, h)
                remain_width -= w
                res = min(res, max_h + dfs(j + 1))
            memo[i] = res
            return memo[i]

        return dfs(0)

    def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:
        # Idea:
        # bottom up of the above

        n = len(books)
        dp = [0 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            remain_width = shelfWidth
            max_h = 0
            res = float("inf")
            for j in range(i, n):
                w, h = books[j]
                if remain_width < w:
                    break
                max_h = max(max_h, h)
                remain_width -= w
                res = min(res, max_h + dp[j + 1])
            dp[i] = res
        return dp[0]


s = Solution()
print(
    s.minHeightShelves(
        books=[[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], shelfWidth=4
    )
)
print(s.minHeightShelves(books=[[1, 3], [2, 4], [3, 2]], shelfWidth=6))

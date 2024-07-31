class Solution:
    def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:
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


s = Solution()
print(
    s.minHeightShelves(
        books=[[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], shelfWidth=4
    )
)
print(s.minHeightShelves(books=[[1, 3], [2, 4], [3, 2]], shelfWidth=6))

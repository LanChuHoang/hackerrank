# https://leetcode.com/problems/coin-change/description/


class Solution:
    def coinChange_v1(self, coins: list[int], amount: int) -> int:
        coins.sort()
        n = len(coins)
        memo = [[-2 for _ in range(amount + 1)] for _ in range(n)]

        def dfs(i: int, left: int):
            if left == 0:
                return 0

            if i >= n and left != 0 or left < 0:
                return -1

            if memo[i][left] != -2:
                return memo[i][left]

            res = float("inf")
            for j in range(i, n):
                if left < coins[j]:
                    break
                choose_j_option = dfs(j, left - coins[j])
                if choose_j_option != -1:
                    res = min(res, choose_j_option)
            res = 1 + res if res != float("inf") else -1
            memo[i][left] = res
            return memo[i][left]

        return dfs(0, amount)

    def coinChange_v2(self, coins: list[int], amount: int) -> int:
        memo = [-1 for _ in range(amount + 1)]

        def dfs(x: int):
            if x < 0:
                return float("inf")
            if x == 0:
                return 0
            if memo[x] != -1:
                return memo[x]
            best = float("inf")
            for c in coins:
                best = min(best, dfs(x - c) + 1)
            memo[x] = best
            return memo[x]

        res = dfs(amount)
        return res if res != float("inf") else -1

    def coinChange(self, coins: list[int], amount: int) -> int:
        memo = [float("inf") for _ in range(amount + 1)]
        memo[0] = 0

        for x in range(1, amount + 1):
            for c in coins:
                if x >= c:
                    memo[x] = min(memo[x], memo[x - c] + 1)
        return memo[amount] if memo[amount] != float("inf") else -1


s = Solution()
print(s.coinChange(coins=[1, 2, 5], amount=11))
print(s.coinChange(coins=[2], amount=3))
print(s.coinChange(coins=[1], amount=0))

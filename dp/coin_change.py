# https://leetcode.com/problems/coin-change/description/


class Solution:
    def coinChange_v1(self, coins: list[int], amount: int) -> int:
        # solve(amount) = min(
        #   solve(amount - c[i]),
        #   solve(amount - c[i + 1])
        #   ...
        #   solve(amount - c[-1])
        # )
        memo = dict()

        def solve(target: int):
            if target == 0:
                return 0

            if target in memo:
                return memo[target]

            min_count = None
            for c in coins:
                if target < c:
                    continue

                use_this_coin = solve(target - c)
                if use_this_coin == -1:
                    continue

                min_count = (
                    min(min_count, use_this_coin + 1)
                    if min_count is not None
                    else use_this_coin + 1
                )
            if min_count is None:
                min_count = -1
            memo[target] = min_count
            return min_count

        return solve(amount)

    def coinChange(self, coins: list[int], amount: int) -> int:
        # bottom up
        dp_table = [amount + 1 for _ in range(amount + 1)]
        dp_table[0] = 0
        for target in range(1, amount + 1):
            for c in coins:
                if target < c:
                    continue

                dp_table[target] = min(dp_table[target], dp_table[target - c] + 1)
        return dp_table[amount] if dp_table[amount] <= amount else -1


# solution = Solution()
# print(solution.coinChange([1, 2, 5], 11))
# print(solution.coinChange([2], 3))
# print(solution.coinChange([1], 0))

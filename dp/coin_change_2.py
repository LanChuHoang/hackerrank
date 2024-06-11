# https://leetcode.com/problems/coin-change-ii/


class Solution:
    # def change_v1(self, amount: int, coins: list[int]) -> int:
    #     # for every amount
    #     # num_solutions(i, amount) =
    #     #   num_solutions(i, amount - coins[i])
    #     #   + num_solutions(i + 1, amount - coins[i + 1])
    #     #   ...
    #     #   + num_solutions(-1, amount - coins[-1])
    #     # only choose coin from i to end to avoid duplicates

    #     coins = sorted(coins)

    #     memo = dict()

    #     def num_solutions(i: int, target: int):
    #         if target == 0:
    #             return 1

    #         if (i, target) in memo:
    #             return memo[(i, target)]

    #         result = 0
    #         for j in range(i, len(coins)):
    #             if target - coins[j] >= 0:
    #                 result += num_solutions(j, target - coins[j])
    #             else:
    #                 break
    #         memo[(i, target)] = result
    #         return result

    #     return num_solutions(0, amount)

    # def change_v2(self, amount: int, coins: list[int]) -> int:
    #     # for every amount
    #     # num_solutions(i, amount) =
    #     #   num_solutions(i, amount - coins[i])
    #     #   + num_solutions(i + 1, amount)
    #     # only choose coin from i to end to avoid duplicates
    #     # -> go bottom-up from num_solutions(-1, 0) -> num_solutions(0, amount)

    #     dp_table = [[0 for _ in range(amount + 1)] for _ in range(len(coins))]

    #     for i in reversed(range(len(coins))):
    #         for target in range(amount + 1):
    #             if target == 0:
    #                 dp_table[i][target] = 1
    #             else:
    #                 if i == 0 and target == 5:
    #                     pass
    #                 if target - coins[i] >= 0:
    #                     dp_table[i][target] += dp_table[i][target - coins[i]]
    #                 if i + 1 < len(coins):
    #                     dp_table[i][target] += dp_table[i + 1][target]
    #     return dp_table[0][amount]

    def change(self, amount: int, coins: list[int]) -> int:
        # Optimization 1: for every iteration, just consider the target from coin -> amount
        # because every target < coin is not makable -> reduce the if condition -> reduce time
        # Optimization 2: only store 1 row and then update -> reduce space
        # amount = 5, coins = [1, 2, 5]
        # Iterations  0   1   2   3   4   5
        # Initial     1   0   0   0   0   0
        # coin 1      1   1   1   1   1   1
        # coin 2      1   1   2   2   3   3
        # coin 3      1   1   2   2   3   4
        dp_table = [0 for _ in range(amount + 1)]
        dp_table[0] = 1
        for c in coins:
            for target in range(c, amount + 1):
                dp_table[target] += dp_table[target - c]
        return dp_table[amount]


# s = Solution()
# print(s.change(5, [1, 2, 5]))
# print(s.change(3, [2]))
# print(s.change(10, [10]))

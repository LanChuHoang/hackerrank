# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # at every i in prices
        # there 3 dicisions:
        #   - Cooldown: profit(i, buyable) = profit(i + 1, buyable)
        #   - Buy immediately: profit(i + 1, buyable=False) - prices[i] if buyable = True
        #   - Sell immediately: profit(i + 2, buyable=True) + prices[i] if buyable = False
        # -> The overall profit at each state (i, buyable)
        # profit(i, buyable) = max(buy/sell immediately, cooldown) if buyable/not buyable

        memo = dict()

        def profit(i: int, buyable: bool):
            if i >= len(prices):
                return 0

            if (i, buyable) in memo:
                return memo[(i, buyable)]

            cooldown_profit = profit(i + 1, buyable)
            if buyable:
                buy_immediately_profit = profit(i + 1, buyable=False) - prices[i]
                memo[(i, buyable)] = max(buy_immediately_profit, cooldown_profit)
            else:
                sell_immediately_profit = profit(i + 2, buyable=True) + prices[i]
                memo[(i, buyable)] = max(sell_immediately_profit, cooldown_profit)
            return memo[(i, buyable)]

        return profit(0, buyable=True)

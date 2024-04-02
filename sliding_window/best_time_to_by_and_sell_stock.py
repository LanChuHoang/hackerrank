# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy_price, max_profit = prices[0], 0

        for p in prices:
            if p > buy_price:
                max_profit = max(p - buy_price, max_profit)
            else:
                buy_price = p

        return max_profit

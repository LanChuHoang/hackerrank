# Best Time to Buy and Sell Stock II


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy_price, total_profit = prices[0], 0

        prev_p = buy_price
        for p in prices:
            if p > prev_p:
                total_profit += p - prev_p
            else:
                buy_price = p
            prev_p = p

        return total_profit

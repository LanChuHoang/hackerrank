# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy_price, sell_price, max_profit = None, None, None
        
        for i in range(len(prices))

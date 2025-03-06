class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        min_price = float('inf')

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit
        
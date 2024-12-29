class Solution(object):
    def maxProfit(self, prices):
        res = 0
        for i in range(len(prices)-1):
            if prices[i] - prices[i+1] > 0:
                continue
            res += prices[i+1] - prices[i]
        
        return res
        
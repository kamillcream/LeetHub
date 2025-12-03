class Solution(object):
    def finalPrices(self, prices):
        stack = []
        ans = prices[:]

        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                j = stack.pop()
                ans[j] = prices[j] - prices[i]
            stack.append(i)

        return ans
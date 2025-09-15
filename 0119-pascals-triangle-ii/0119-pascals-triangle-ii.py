class Solution(object):
    def getRow(self, rowIndex):
        dp = [0] * (rowIndex + 1)
        dp[0] = 1
        for i in range(1, rowIndex + 1):
            for j in range(i, 0, -1):   # 역순 업데이트가 핵심
                dp[j] += dp[j-1]
        return dp
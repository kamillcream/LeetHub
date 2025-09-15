class Solution(object):
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]

        if rowIndex == 1:
            return [1,1]

        dp = [1,1] + [0] * (rowIndex - 2 + 1)
        for i in range(2, rowIndex+1):
            for j in range(i, -1, -1):
                if j == i or j == 0: 
                    dp[j] = 1
                else:
                    dp[j] += dp[j-1]

        
        return dp



        return dp[rowIndex] 

        
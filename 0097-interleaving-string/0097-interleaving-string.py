class Solution(object):
    def isInterleave(self, s1, s2, s3):
        n, m, l = len(s1), len(s2), len(s3)

        if n+m != l:
            return False

        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n+1):
            dp[i] = dp[i-1] and s1[i-1] == s3[i-1]

        for i in range(1, m+1):
            dp[0] = dp[0] and s2[i-1] == s3[i-1]
            for j in range(1, n+1):
                dp[j] = (dp[j] and s2[i-1] == s3[i+j-1]) \
                    or (dp[j-1] and s1[j-1] == s3[i+j-1])

        return dp[n]



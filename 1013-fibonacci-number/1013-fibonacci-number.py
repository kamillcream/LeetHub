class Solution(object):
    dp = collections.defaultdict(int)
    def fib(self, n):
        if n <= 1:
            return n

        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.fib(n-1) + self.fib(n-2)
        return self.dp[n]
        
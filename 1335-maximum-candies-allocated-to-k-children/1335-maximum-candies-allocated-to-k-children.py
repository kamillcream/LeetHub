class Solution(object):
    def maximumCandies(self, candies, k):
        if sum(candies) < k:
            return 0
        
        left, right = 1, max(candies)
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            count = sum(c // mid for c in candies)

            if count >= k:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans

        
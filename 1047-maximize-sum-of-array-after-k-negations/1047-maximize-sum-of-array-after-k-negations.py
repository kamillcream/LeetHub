class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        heapq.heapify(nums)

        while k > 0:
            min_value = heapq.heappop(nums)
            heapq.heappush(nums, -min_value)
            k -= 1

        return sum(nums)
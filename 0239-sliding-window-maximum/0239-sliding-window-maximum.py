class Solution(object):
    def maxSlidingWindow(self, nums, k):
        results = []
        deque = collections.deque()

        for i in range(len(nums)):
            if deque and deque[0] < i - k + 1:
                deque.popleft()

            while deque and nums[deque[-1]] < nums[i]:
                deque.pop()

            deque.append(i)

            if i >= k - 1:
                results.append(nums[deque[0]])

        return results
        
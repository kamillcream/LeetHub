class Solution(object):
    def maxSlidingWindow(self, nums, k):
        results = []
        deque = collections.deque()

        for i in range(len(nums)):
            # 윈도우 범위 벗어난 값들 제거
            # ex. deque[0] = 3, i = 4 , k = 1 이면 너비가 1인 윈도우가 4번째에 있으므로 3은 벗어난 거.  
            if deque and deque[0] < i - k + 1:
                deque.popleft()

            # 새로운 값들보다 작은 값들 제거
            # 새로 들어온 값보다 작다면 앞으로도 최댓값이 될 수 없음.
            while deque and nums[deque[-1]] < nums[i]:
                deque.pop()

            deque.append(i)

            if i >= k - 1:
                results.append(nums[deque[0]])

        return results
        
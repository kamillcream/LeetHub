class Solution(object):
    def minEatingSpeed(self, piles, h):
        left, right = 1, max(piles)  
        answer = right 
        while left <= right:
            mid = (left + right) // 2  
            hours_needed = sum((p + mid - 1) // mid for p in piles)  # 올림 연산으로 시간 계산

            if hours_needed <= h:  # h 시간 내에 먹을 수 있다면 더 작은 k 가능
                answer = mid
                right = mid - 1
            else:  # 시간이 부족하다면 더 큰 k 필요
                left = mid + 1

        return answer
from collections import deque
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        # 숫자를 문자열로 변환하여 리스트로 만든다
        x = str(x)
        
        nums = deque(x)  # deque로 변환
        while len(nums) > 1:
            if nums.popleft() != nums.pop():  # 양끝의 값을 비교
                return False  # 불일치 시 False 반환
        return True  # 전체 비교가 끝난 후 True 반환
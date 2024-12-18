class Solution(object):
    def isPalindrome(self, x):
        # 음수인 경우 팰린드롬이 될 수 없다.
        if x < 0:
            return False
        
        # 숫자를 문자열로 변환하여 앞뒤 비교
        str_x = str(x)
        left, right = 0, len(str_x) - 1
        
        while left < right:
            if str_x[left] != str_x[right]:
                return False
            left += 1
            right -= 1
        
        return True
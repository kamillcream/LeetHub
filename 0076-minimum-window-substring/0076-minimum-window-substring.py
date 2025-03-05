class Solution(object):
    def minWindow(self, s, t):
        need = collections.Counter(t) # 단어 내 각각의 문자 개수
        missing = len(t) # 전체 단어 길이
        start = left = end = 0

        # 오른쪽 포인터 이동
        for right, char in enumerate(s, 1):
            missing -= need[char] > 0 # 필요한 문자가 need[char]에 있으면 전체 길이에서 -1
            need[char] -= 1 # 그 후 해당 문자의 필요한 개수 -1

            # 필요 문자가 0이면 왼쪽 포인터 이동
            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                if not end or right - left <= end - start:
                    start, end = left, right
                    need[s[left]] += 1
                    missing += 1
                    left +=1
        return s[start:end]
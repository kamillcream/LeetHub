class Solution(object):
    def balancedStringSplit(self, s):
        cnt = 0
        res = 0

        for i in s:
            cnt += 1 if i == 'L' else -1
            if cnt == 0:
                res += 1
        return res
        
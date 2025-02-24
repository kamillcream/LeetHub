class Solution(object):
    def balancedStringSplit(self, s):
        sub = []
        res = 0

        for i in s:
            sub.append(i)
            if sub.count('L') == sub.count('R'):
                res += 1
                sub = []
        
        return res
        
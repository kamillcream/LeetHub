class Solution(object):
    def diStringMatch(self, s):
        low, high = 0, len(s)
        perm = []

        for char in s:
            if char == "I":
                perm.append(low)
                low += 1
            elif char == "D":
                perm.append(high)
                high -=  1
        perm.append(low)
        return perm
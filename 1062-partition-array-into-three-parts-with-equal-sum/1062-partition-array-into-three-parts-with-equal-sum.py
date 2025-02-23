class Solution(object):
    def canThreePartsEqualSum(self, arr):
        if sum(arr) % 3 != 0:
            return False
        target = sum(arr) / 3

        partial = 0
        cnt = 0

        for i in range(len(arr)):
            partial += arr[i]
            if partial == target:
                cnt += 1
                partial = 0
                if cnt == 3:
                    return True
            if i == len(arr) - 1:
                return False
        
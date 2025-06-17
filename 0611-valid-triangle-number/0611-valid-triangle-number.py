class Solution(object):
    def triangleNumber(self, nums):
        nums.sort()
        n = len(nums)
        cnt = 0

        for i in range(n - 1, 1, -1):
            j, k = 0, i - 1

            while j < k:
                if nums[j] + nums[k] > nums[i]:
                    cnt += k - j
                    k -= 1
                else:
                    j += 1
        return cnt

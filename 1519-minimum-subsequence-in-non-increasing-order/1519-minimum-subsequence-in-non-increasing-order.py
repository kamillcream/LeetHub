class Solution(object):
    def minSubsequence(self, nums):
        nums.sort(reverse = True)
        sub = []
        total = sum(nums)
        sub_sum = 0
        for i in nums:
            sub.append(i)
            sub_sum += i
            if sub_sum > total - sub_sum:
                break
        return sub        
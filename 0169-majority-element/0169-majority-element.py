class Solution(object):
    def majorityElement(self, nums):
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        half = len(nums) // 2

        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])

        return [b, a] [nums.count(a) > half]
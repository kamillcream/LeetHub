
class Solution(object):
    def largestNumber(self, nums):
        nums = list(map(str, nums))
        nums.sort(key = lambda x : x * 10, reverse=True)
        result = "".join(nums)


        return "0" if nums[0] == "0" else "".join(nums)
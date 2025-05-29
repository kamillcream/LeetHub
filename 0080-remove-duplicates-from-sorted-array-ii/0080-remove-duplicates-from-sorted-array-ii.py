class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        i = 2  
        for j in range(2, len(nums)):
            # 2번째 앞 칸이랑 같으면 제거해야 함.
            if nums[j] != nums[i - 2]:
                nums[i] = nums[j]
                i += 1
        
        return i
                

        
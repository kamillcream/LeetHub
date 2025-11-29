class Solution(object):
    def findDisappearedNumbers(self, nums):
        size = len(nums)
        set_nums = set(nums)
        answer = []
        
        for i in range(1, size + 1):
            if i not in set_nums:
                answer.append(i)


        return answer


        
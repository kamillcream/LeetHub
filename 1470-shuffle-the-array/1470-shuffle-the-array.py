class Solution(object):
    def shuffle(self, nums, n):
        answer = []
        nums_first_half = nums[:n]
        nums_second_half = nums[n:]

        for i in range(n):
            answer.append(nums_first_half[i])
            answer.append(nums_second_half[i])

        return answer
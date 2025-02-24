class Solution(object):
    def jump(self, nums):
        n = len(nums)
        if n == 1:
            return 0

        jumps = 0
        max_reach = 0
        last_jump_end = 0

        for i in range(len(nums)-1):
            max_reach = max(max_reach, i + nums[i])

            if i == last_jump_end:
                jumps += 1
                last_jump_end = max_reach
            
                if last_jump_end >= n - 1:
                    break
        return jumps
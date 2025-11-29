class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        nums_string = ''.join(map(str, nums))
        lengths = [len(p) for p in nums_string.split('0')]

        return max(lengths)
        
            
        
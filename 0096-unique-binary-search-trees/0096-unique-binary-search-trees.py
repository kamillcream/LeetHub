from functools import lru_cache

class Solution(object):
    def numTrees(self, n):

        @lru_cache(None)  
        def count(num):
            if num <= 1:
                return 1

            total = 0
            for i in range(1, num + 1):
                left_sum = count(i - 1)
                right_sum = count(num - i)  
                total += left_sum * right_sum  

            return total

        return count(n)
class Solution(object):
    def numTrees(self, n):
        memo = {}  

        def count(num):
            if num <= 1:
                return 1

            if num in memo: 
                return memo[num]

            total = 0
            for i in range(1, num + 1):
                left_sum = count(i - 1)  
                right_sum = count(num - i) 
                total += left_sum * right_sum 
            
            memo[num] = total 
            return total

        return count(n)
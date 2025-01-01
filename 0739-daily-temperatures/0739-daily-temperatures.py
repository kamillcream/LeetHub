class Solution(object):
    def dailyTemperatures(self, temperatures):
        ans = [0] * len(temperatures)
        stack = []
        for i, cur in enumerate(temperatures):
            while stack and cur > temperatures[stack[-1]]:
                last = stack.pop()
                ans[last] = i -last
            stack.append(i)
        return ans

    
        
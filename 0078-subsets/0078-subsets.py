class Solution(object):
    def subsets(self, nums):
        res = []
        
        def dfs(index, path):
            res.append(path)

            for i in range(index, len(nums)):
                dfs(i+1, path + [nums[i]])

        dfs(0,[])
        return res
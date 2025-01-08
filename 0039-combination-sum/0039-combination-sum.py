class Solution(object):
    def combinationSum(self, candidates, target):
        res = []

        def dfs(csum, index, path):
            if csum < 0:
                return
            if csum == 0:
                res.append(path)
                return
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])

        dfs (target, 0, [])
        return res
        
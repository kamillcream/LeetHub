class Solution(object):
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()

        def dfs(csum, index, path):
            if csum < 0:
                return
            if csum == 0:
                res.append(path)
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                dfs(csum - candidates[i], i+1, path + [candidates[i]])

        dfs(target, 0, [])
        return res
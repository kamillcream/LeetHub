class Solution(object):
    def combinationSum(self, candidates, target):
        def dfs(index, current, total):
            if total == target:
                result.append(list(current))
                return
            
            if total > target:
                return
            
            for i in range(index, len(candidates)):
                current.append(candidates[i])
                dfs(i, current, total + candidates[i])
                current.pop() # 백트래킹
        result = []
        dfs(0,[],0)
        return result
class Solution(object):
    def permuteUnique(self, nums):
        res = []
        nums.sort()  # 중복 제거를 위해 정렬
        visited = [False] * len(nums)  # 방문 여부 추적
        
        def dfs(path):
            if len(path) == len(nums):  # 경로가 nums와 길이가 같으면 결과에 추가
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                # 중복된 숫자는 건너뛰기
                if visited[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue
                
                visited[i] = True
                dfs(path + [nums[i]])  # 다음 경로 탐색
                visited[i] = False
        
        dfs([])
        return res

class Solution:
    def generate(self, numRows):
        res = [[1]]  # 첫 번째 행은 항상 [1]
        
        for i in range(1, numRows):  # 두 번째 행부터 시작
            row = [1]  # 각 행의 첫 번째 원소는 1
            for j in range(1, i):  # 중간 값 계산
                row.append(res[i-1][j-1] + res[i-1][j])
            row.append(1)  # 각 행의 마지막 원소는 1
            res.append(row)
        
        return res
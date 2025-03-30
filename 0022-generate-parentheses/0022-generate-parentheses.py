class Solution(object):
    def generateParenthesis(self, n):
        result = []

        def backtrack(open_count, close_count, path):
            # 종료 조건
            if open_count == n and close_count == n:
                result.append(path)
                return
            
            # 여는 괄호 추가 가능할 때
            if open_count < n:
                backtrack(open_count + 1, close_count, path + "(")
            
            # 닫는 괄호 추가 가능할 때
            if close_count < open_count:
                backtrack(open_count, close_count + 1, path + ")")
        
        backtrack(0, 0, "")
        return result
class Solution(object):
    def exist(self, board, word):
        def dfs(inI, inJ, index):
            if index == len(word):
                return True
            
            if inI < 0 or inJ < 0 or inI >= len(board) or inJ >= len(board[0]) or board[inI][inJ] != word[index]:
                return False

            temp = board[inI][inJ]
            board[inI][inJ] = "#"


            found = (dfs(inI+1, inJ, index + 1) or
                dfs(inI-1, inJ, index + 1) or 
                dfs(inI, inJ+1, index + 1) or
                dfs(inI, inJ-1, index+1)
            )
            board[inI][inJ] = temp

            return found

        if not board or not word:
            return False


        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0):
                    return True
        return False
        
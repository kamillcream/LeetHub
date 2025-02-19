class Solution(object):
    def largestValues(self, root):
        self.res = [] 
        def dfs(row, node):
            if not node:
                return
            if len(self.res) <= row:
                self.res.append(node.val)
            else:
                self.res[row] = max(self.res[row], node.val)
            
            dfs(row + 1, node.left)
            dfs(row + 1, node.right)

        dfs(0, root)
        return self.res


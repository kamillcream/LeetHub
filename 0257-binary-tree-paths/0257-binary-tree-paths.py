class Solution(object):
    def binaryTreePaths(self, root):
        if not root:
            return []

        self.res = []
        def dfs(cur,t):
            if not t:
                return
            cur.append(str(t.val))
            
            if not t.left and not t.right:
                self.res.append("->".join(cur))

            dfs(cur, t.left)
            dfs(cur, t.right)
            
            cur.pop()


        dfs([], root)
        return self.res
        
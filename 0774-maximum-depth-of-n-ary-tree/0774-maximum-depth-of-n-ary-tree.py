class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0

        self.res = 0

        def dfs(cur_depth, node):
            if not node:
                return 

            if not node.children:
                self.res = max(self.res, cur_depth)

            for i in node.children:
                dfs(cur_depth+1, i)

        dfs(1, root)
        return self.res
        
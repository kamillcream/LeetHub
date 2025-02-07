class Solution(object):
    def maxPathSum(self, root):
        self.max_sum = float('-inf')
        def dfs(node):
            if not node:
                return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            self.max_sum = max(self.max_sum, left + right + node.val)

            return max(left, right) + node.val
        dfs(root)
        return self.max_sum
            
        
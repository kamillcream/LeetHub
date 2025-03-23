class Solution(object):
    def sumNumbers(self, root):
        if not root:
            return

        def dfs(node, cur_value):
            if not node:
                return 0
            
            cur_value = cur_value * 10 + node.val

            if not node.left and not node.right:
                return cur_value
            
            return dfs(node.left, cur_value) + dfs(node.right, cur_value)
            
            
        return dfs(root, 0)

            
        
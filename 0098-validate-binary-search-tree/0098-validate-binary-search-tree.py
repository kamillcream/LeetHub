class Solution(object):
    def isValidBST(self, root):
        def dfs(node, min_val, max_val):
            if not node:
                return True
            
            if (min_val is not None and node.val <= min_val) or \
                (max_val is not None and node.val >= max_val):
                return False
            return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)

        return dfs(root, None, None)

class Solution(object):
    def pathSum(self, root, targetSum):
        result = []

        def dfs(node, curr_sum, path):
            if not node:
                return
            
            curr_sum += node.val
            path.append(node.val)

            if not node.left and not node.right and curr_sum == targetSum:
                result.append(list(path))

            dfs(node.left, curr_sum, path)
            dfs(node.right, curr_sum, path)

            path.pop()  # 백트래킹

        dfs(root, 0, [])
        return result
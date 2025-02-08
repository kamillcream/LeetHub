class Solution(object):
    def pathSum(self, root, targetSum):
        self.res = 0
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1

        def dfs(node, cur_sum):
            if not node:
                return

            cur_sum += node.val
            self.res += prefix_sum[cur_sum - targetSum]

            prefix_sum[cur_sum] += 1

            dfs(node.left, cur_sum)
            dfs(node.right, cur_sum)

            prefix_sum[cur_sum] -= 1
        dfs(root, 0)
        return self.res


            

        
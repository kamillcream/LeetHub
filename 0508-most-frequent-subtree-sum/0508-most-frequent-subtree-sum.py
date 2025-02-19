class Solution(object):
    def findFrequentTreeSum(self, root):
        self.res = defaultdict(int)

        def dfs(node):
            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            cur_sum = node.val + left_sum + right_sum

            self.res[cur_sum] += 1

            return cur_sum


        dfs(root)

        max_freq = max(self.res.values())
        most_frequent_sums = [key for key, val in self.res.items() if val == max_freq]
        
        return most_frequent_sums

        
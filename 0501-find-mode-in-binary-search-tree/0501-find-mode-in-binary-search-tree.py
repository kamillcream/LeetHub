from collections import defaultdict

class Solution(object):
    def findMode(self, root):
        self.cnt = 0
        self.dict = defaultdict(int)

        def dfs(node):
            if not node:
                return
            self.dict[node.val] += 1  # 기존 값이 있으면 +1, 없으면 기본값 0에서 +1
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        max_freq = max(self.dict.values())

        return [key for key, val in self.dict.items() if val == max_freq]
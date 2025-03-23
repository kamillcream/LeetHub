class Solution(object):
    def rightSideView(self, root):
        res = []

        def dfs(node, depth):
            if not node:
                return

            # 현재 depth에 처음 도달한 노드면 추가
            if depth == len(res):
                res.append(node.val)

            # 먼저 오른쪽 방문
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return res
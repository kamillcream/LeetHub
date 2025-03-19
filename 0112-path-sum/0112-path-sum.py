class Solution(object):
    def hasPathSum(self, root, targetSum):
        def dfs(node, cur_sum):
            if not node:
                return False
            
            cur_sum += node.val

            # 리프 노드 도달 시, 합이 targetSum인지 확인
            if not node.left and not node.right:
                return cur_sum == targetSum

            # 왼쪽 또는 오른쪽 서브트리에 만족하는 경로가 있는지 확인
            return dfs(node.left, cur_sum) or dfs(node.right, cur_sum)
        
        return dfs(root, 0)
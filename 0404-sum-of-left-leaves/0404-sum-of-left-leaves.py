class Solution(object):
    def sumOfLeftLeaves(self, root):
        self.res = 0  # 왼쪽 잎 노드 값의 합을 저장하는 변수

        if not root:
            return 0  # 빈 트리라면 0 반환

        def dfs(node, is_left):
            if not node:  # 노드가 None이면 리턴 (AttributeError 방지)
                return
            
            # 리프 노드이고, 왼쪽 자식인 경우 res에 더함
            if not node.left and not node.right and is_left:
                self.res += node.val
            
            # 왼쪽과 오른쪽 서브트리 탐색
            dfs(node.left, True)   # 왼쪽 자식 탐색 (is_left=True)
            dfs(node.right, False) # 오른쪽 자식 탐색 (is_left=False)

        dfs(root, False)  # 루트는 왼쪽 잎이 아니므로 False로 시작
        return self.res  # 최종 결과 반환
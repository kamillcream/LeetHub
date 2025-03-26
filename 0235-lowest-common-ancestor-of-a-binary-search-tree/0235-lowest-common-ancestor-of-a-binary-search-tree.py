class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        # 둘 다 왼쪽에 있는 경우
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        # 둘 다 오른쪽에 있는 경우
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        # 둘이 다른 방향 or root 중 하나가 p/q → root가 LCA
        else:
            return root
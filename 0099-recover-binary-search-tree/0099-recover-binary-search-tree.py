class Solution(object):
    def recoverTree(self, root):
        self.first = None
        self.second = None
        self.prev = None

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)

            # 중위 순회 중 잘못된 노드 찾기
            if self.prev and self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev
                self.second = node
            
            self.prev = node
            inorder(node.right)
        inorder(root)

        if self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val
        
        
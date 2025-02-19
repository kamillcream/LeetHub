class Solution(object):
    def getMinimumDifference(self, root):
        self.res = float('INF')
        self.prev = None
        def inorder(node):
            if not node:
                return
            inorder(node.left)

            if self.prev is not None:
                self.res = min(abs(node.val - self.prev), self.res)
            
            self.prev = node.val
            inorder(node.right)

        inorder(root)

        return self.res
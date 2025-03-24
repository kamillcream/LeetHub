class Solution(object):
    def kthSmallest(self, root, k):
        self.k = k
        self.res = None

        def inorder(node):
            if not node or self.res is not None:
                return

            inorder(node.left)

            self.k -= 1
            if self.k == 0:
                self.res = node.val
                return

            inorder(node.right)

        inorder(root)
        return self.res
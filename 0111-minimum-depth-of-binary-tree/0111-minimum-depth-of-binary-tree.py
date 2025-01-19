class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        if not root.left or not root.right:
            return max(left, right) + 1

        return min(left, right) + 1

        

        
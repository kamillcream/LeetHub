# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTilt(self, root):
        if not root:
            return 0

        self.total_tilt = 0

        self.dfs(root)

        return self.total_tilt

    def dfs(self, node):
        if not node:
            return 0
        
        left_sum = self.dfs(node.left)
        right_sum = self.dfs(node.right)

        self.total_tilt += abs(left_sum - right_sum)

        return left_sum + right_sum + node.val
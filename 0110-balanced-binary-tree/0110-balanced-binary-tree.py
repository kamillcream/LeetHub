class Solution(object):
    def isBalanced(self, root):
        def check(root):
            if not root:
                return 0
            
            left = check(root.left)
            right = check(root.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            
            return max(left, right) + 1

        return check(root) != -1
        
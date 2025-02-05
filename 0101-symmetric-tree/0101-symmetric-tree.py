class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True

        def isMirror(n1, n2):
            if not n1 and not n2: return True
            if not n1 or not n2: return False
            if n1.val != n2.val: return False

            return isMirror(n1.left, n2.right) and isMirror(n1.right, n2.left)
        return isMirror(root.left, root.right)
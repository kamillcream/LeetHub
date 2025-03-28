class Solution(object):
    def findBottomLeftValue(self, root):
        if not root:
            return None

        queue = deque([root])
        leftmost = None

        while queue:
            lvl_size = len(queue)

            for i in range(lvl_size):
                node = queue.popleft()
                if i == 0:
                    leftmost = node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return leftmost
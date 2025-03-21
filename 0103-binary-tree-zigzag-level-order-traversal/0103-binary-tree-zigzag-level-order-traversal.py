class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        res = []
        queue = deque([root])
        is_zigzag = False

        while queue:
            lvl_size = len(queue)
            lvl_nodes = []

            for _ in range(lvl_size):
                node = queue.popleft()
                if is_zigzag:
                    lvl_nodes.insert(0, node.val)
                else:
                    lvl_nodes.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                
            is_zigzag = not is_zigzag
            res.append(lvl_nodes)

        return res        
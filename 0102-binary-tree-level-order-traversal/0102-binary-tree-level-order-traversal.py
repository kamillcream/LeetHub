class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        
        res = []
        queue = deque([root])

        while queue:
            lvl_size = len(queue)
            lvl_nodes = []

            for _ in range(lvl_size):
                node = queue.popleft()
                lvl_nodes.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)


            res.append(lvl_nodes)
        return res

        
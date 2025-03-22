class Solution(object):
    def connect(self, root):
        if not root:
            return None

        queue = deque([root])

        while queue:
            lvl_size = len(queue)
            prev = None
            for _ in range(lvl_size):
                node = queue.popleft()
                if prev:
                    prev.next = node
                prev = node
            
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)


        return root
        
        
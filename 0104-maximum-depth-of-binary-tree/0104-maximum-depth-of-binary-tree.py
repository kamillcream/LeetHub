class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        
        queue = collections.deque([root])
        depth = 0

        while queue:
            depth += 1
            for i in range(len(queue)):
                cur_root = queue.popleft()
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)

        return depth
        
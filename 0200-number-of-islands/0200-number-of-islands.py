class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0, -1)]
        cnt = 0

        def bfs(i, j):
            queue = collections.deque([(i,j)])
            grid[i][j] = '0'

            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nX = x + dx
                    nY = y + dy
                    if 0 <= nX < rows and 0 <= nY < cols and grid[nX][nY] == '1':
                        grid[nX][nY] = '0'
                        queue.append((nX, nY))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    bfs(i, j)
                    cnt += 1

        return cnt
from collections import deque

class Solution:
    def bfs(self, grid, rows, cols, pos):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        queue = deque([pos])

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == "0":
                    continue
                
                queue.append((nr, nc))
                grid[nr][nc] = "0"


    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    self.bfs(grid, rows, cols, (r, c))
                    count += 1 

        return count
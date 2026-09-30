from collections import deque

class Solution:
    def bfs(self, grid, rows, cols, pos, visited):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        queue = deque([pos])

        while queue:
            r, c = queue.popleft()
            visited.add((r, c))

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == "0":
                    continue
                
                if (nr, nc) not in visited:
                    queue.append((nr, nc))
                    visited.add((nr, nc))


    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    self.bfs(grid, rows, cols, (r, c), visited)
                    count += 1 

        return count
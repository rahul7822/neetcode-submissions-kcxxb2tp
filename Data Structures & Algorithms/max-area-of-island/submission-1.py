from collections import deque

class Solution:
    def bfs(self, grid, rows, cols, pos):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        area = 1
        queue = deque([pos])
        grid[pos[0]][pos[1]] = 0

        while queue:   
            r, c = queue.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == 0:
                    continue

                queue.append((nr, nc))
                grid[nr][nc] = 0
                area += 1

        return area


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        max_area = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    cur_area = self.bfs(grid, rows, cols, (r, c))
                    print(cur_area)
                    max_area = max(max_area, cur_area)

        return max_area
from collections import deque

class Solution:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    queue.append((r,c))
                    visited.add((r,c))
                    break

        total_perimeter = 0

        while queue:
            r, c = queue.popleft()

            for dr, dc in self.directions:
                nr, nc = dr + r, dc + c
                
                if (nr,nc) in visited:
                    continue

                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == 0:
                    total_perimeter += 1
                else:
                    queue.append((nr,nc))
                    visited.add((nr,nc))
        
        return total_perimeter

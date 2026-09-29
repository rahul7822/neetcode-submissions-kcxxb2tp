class Solution:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def get_perimeter(self, grid, pos, rows, cols):
        x, y = pos
        perimeter = 0

        for dr, dc in self.directions:
            nr = x + dr
            nc = y + dc

            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == 0:
                perimeter += 1
        
        return perimeter


    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        total_perimeter = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    total_perimeter += self.get_perimeter(grid, (r,c), rows, cols) 
        
        return total_perimeter

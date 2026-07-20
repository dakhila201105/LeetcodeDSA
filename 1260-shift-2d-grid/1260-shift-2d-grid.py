class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        total_cells = m * n
        k %= total_cells
        
        flat_grid = [val for row in grid for val in row]
        shifted_flat = flat_grid[-k:] + flat_grid[:-k] if k > 0 else flat_grid
        
        return [shifted_flat[i * n : (i + 1) * n] for i in range(m)]
        
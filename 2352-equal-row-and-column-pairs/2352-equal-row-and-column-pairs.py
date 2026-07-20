class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n=len(grid)
        pair_count=0
        for r in range(n):
            for c in range(n):
                is_equal=True
                for i in range(n):
                    if grid[r][i]!=grid[i][c]:
                        is_equal=False
                        break
                if is_equal:
                    pair_count+=1
        return pair_count



                
        
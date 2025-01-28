class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        max_score = 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = [[False] * COLS for _ in range(ROWS)]
        def dfs(r, c):
            if (r == ROWS or r < 0 or c == COLS or c < 0 
            or grid[r][c] == 0 or visited[r][c]):
                return 0
            else :
                visited[r][c] = True
                res = grid[r][c]
                nei = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
                for nr, nc in nei:
                    res += dfs(nr, nc)
                return res
        for r in range(ROWS):
            for c in range(COLS):
                max_score = max(max_score, dfs(r, c))
        return max_score
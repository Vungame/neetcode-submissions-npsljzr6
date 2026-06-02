class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        currentMax = 0

        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col):
            if(row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == 0):
                return 0
            
            grid[row][col] = 0
            count = 1
            for dr, dc in directions: 
                count += dfs(row + dr, col + dc)
            
            return count

        for r in range(rows):
            for c in range(cols):
                if(grid[r][c] == 1):
                    currentMax = max(dfs(r,c), currentMax)

        return currentMax

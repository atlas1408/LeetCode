class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rowMax = len(grid)
        colMax = len(grid[0])
        islands = 0
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(pos):
            for direction in directions:
                newX, newY = pos[0]+direction[0], pos[1]+direction[1]
                if 0<=newX<rowMax and 0<=newY<colMax and grid[newX][newY] == "1":
                    grid[newX][newY] = "0"
                    dfs((newX, newY))

        for row in range(rowMax):
            for col in range(colMax):
                if grid[row][col] == "1":
                    grid[row][col] = "0"
                    dfs((row,col))
                    islands+=1
        return islands
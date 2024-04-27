class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp={}

        ROWS, COLS=len(grid),len(grid[0])
        addition=0
        for r in range(ROWS-1,-1,-1):
            addition+=grid[r][COLS-1]
            dp[(r,COLS-1)]=addition
        
        addition=0
        for c in range(COLS-1,-1,-1):
            addition+=grid[ROWS-1][c]
            dp[(ROWS-1,c)]=addition
        
        def solve(r,c):
            if (r,c) in dp:
                return dp[(r,c)]
            
            dp[(r,c)]=grid[r][c]+min(solve(r+1,c),solve(r,c+1))

            return dp[(r,c)]
        
        return solve(0,0)

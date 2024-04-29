class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp={}

        for r in range(m):
            dp[(r,n-1)]=1
        
        for c in range(n):
            dp[(m-1,c)]=1

        
        def solve(x,y):
            if (x,y) in dp:
                return dp[(x,y)]
            

            dp[(x,y)]=solve(x+1,y)+solve(x,y+1)
            return dp[(x,y)]
        
        return solve(0,0)

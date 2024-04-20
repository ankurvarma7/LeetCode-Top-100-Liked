class Solution:
    def numSquares(self, n: int) -> int:
        dp={}
        dp[0]=0
        dp[1]=1
        def solve(n):
            if n in dp:
                return dp[n]
            
            dp[n]=float('inf')
            for i in range(1,n):
                if i*i>n:
                    break
                dp[n]=min(dp[n],1+solve(n-(i*i)))
            
            return dp[n]
        
        return solve(n)

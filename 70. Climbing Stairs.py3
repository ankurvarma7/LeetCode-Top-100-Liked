class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2

        
        dp={}
        dp[1]=1
        dp[2]=2

        def solve(n):
            if n in dp:
                return dp[n]
            
            dp[n]=solve(n-1)+solve(n-2)
            return dp[n]
        
        return solve(n)

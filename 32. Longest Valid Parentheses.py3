class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp=collections.defaultdict(int)
        ans=0
        for i in range(1,len(s)):
            if s[i]==')':
                if s[i-1]=='(':
                    dp[i]=2+dp[i-2]
                
                elif s[i-1]==')':
                    x=dp[i-1]
                    if i-x-1>=0 and s[i-x-1]=='(':
                        dp[i]=x+2+dp[i-x-2]

            ans=max(ans,dp[i])


        return ans

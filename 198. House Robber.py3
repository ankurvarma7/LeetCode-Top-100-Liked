class Solution:
    def rob(self, nums: List[int]) -> int:
        dp={}

        dp[0]=nums[0]

        def solve(index):
            if index<0:
                return 0
            if index in dp:
                return dp[index]
            
            dp[index]=max(nums[index]+solve(index-2),solve(index-1))
            return dp[index]
        
        return solve(len(nums)-1)

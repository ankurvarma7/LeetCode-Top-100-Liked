class Solution:
    def canJump(self, nums: List[int]) -> bool:

        dp={}

        dp[len(nums)-1]=True

        def solve(index):
            if index>=len(nums):
                return True
            
            if index in dp:
                return dp[index]
            
            dp[index]=False
            
            if nums[index]==0:
                return False
            
            for i in range(nums[index],0,-1):
                if solve(index+i):
                    dp[index]=True
                    break
            
            return dp[index]

        
        return solve(0)

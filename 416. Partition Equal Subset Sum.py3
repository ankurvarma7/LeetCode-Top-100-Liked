class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=0
        for num in nums:
            total+=num
        
        if total%2!=0:
            return False
        
        half=total//2
        dp={}
        def solve(index,s):
            if s==0:
                return True
            
            if index<0:
                return False

            if (index,s) in dp:
                return dp[(index,s)]
            
            dp[(index,s)]=solve(index-1,s)

            if nums[index]<=s:
                dp[(index),s]=dp[(index,s)] or solve(index-1,s-nums[index])
            

            return dp[(index,s)]
            
        return solve(len(nums)-1,half)

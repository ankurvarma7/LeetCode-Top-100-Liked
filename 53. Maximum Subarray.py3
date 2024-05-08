class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum=float('-inf')
        add=0

        i=0
        j=0

        while j<len(nums):
            add+=nums[j]
            maxSum=max(maxSum,add)
            if add<0:
                add=0
                i=j+1
            j+=1
        
        return maxSum

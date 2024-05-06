class Solution:
    def findMin(self, nums: List[int]) -> int:
        length=len(nums)
        if length==1:
            return nums[0]
        
        if nums[0]<nums[length-1]:
            return nums[0]

        if nums[length-1]<nums[length-2]:
            return nums[length-1]
        
        l=1
        r=length-2

        while l<=r:
            m=(l+r)//2
            if nums[m]<nums[m-1] and nums[m]<nums[m+1]:
                return nums[m]
            elif nums[m]>nums[0]:
                l=m+1
            else:
                r=m-1

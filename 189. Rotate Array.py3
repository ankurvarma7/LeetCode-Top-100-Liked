class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(st,en):
            while st<en:
                temp=nums[st]
                nums[st]=nums[en]
                nums[en]=temp
                st+=1
                en-=1
        
        k=k%(len(nums))
        reverse(0,len(nums)-1)
        reverse(0,k-1)
        reverse(k,len(nums)-1)

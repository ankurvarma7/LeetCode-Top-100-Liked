class Solution:
    def sortColors(self, nums: List[int]) -> None:
        freq=[0]*3

        for num in nums:
            freq[num]+=1
        index=0
        for i in range(3):
            while freq[i]>0:
                nums[index]=i
                freq[i]-=1
                index+=1

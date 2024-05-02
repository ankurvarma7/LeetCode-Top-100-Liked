class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res=[]

        def swap(i,j):
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp
        
        def getPermutations(index):
            if index==len(nums):
                res.append(nums.copy())
                return
            
            for i in range(index,len(nums)):
                swap(index,i)
                getPermutations(index+1)
                swap(index,i)
    
        getPermutations(0)
        return res

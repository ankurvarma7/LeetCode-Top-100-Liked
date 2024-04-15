class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        curr=[]

        index=0

        def getSubsets(index):
            if index==len(nums):
                ans.append(curr.copy())
                return

            curr.append(nums[index])
            getSubsets(index+1)
            curr.pop()
            getSubsets(index+1)
        
        getSubsets(0)
        return ans

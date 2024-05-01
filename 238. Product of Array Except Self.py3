class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        allproduct=1
        countzero=0
        index=0
        for i,n in enumerate(nums):
            if n==0:
                countzero+=1
                index=i
                continue
            
            allproduct*=n
        
        if countzero>1:
            return [0]*len(nums)
        
        if countzero==1:
            res=[0]*len(nums)
            res[index]=allproduct
            return res
        
        res=[]
        for n in nums:
            res.append(allproduct//n)
        
        return res

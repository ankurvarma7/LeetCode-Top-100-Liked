class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        prevIndex=len(nums)-1
        currIndex=len(nums)-2

        while(currIndex>=0):
            if nums[prevIndex]>nums[currIndex]:
                swapIndex=len(nums)-1
                while(swapIndex>currIndex and nums[swapIndex]<=nums[currIndex]):
                    swapIndex-=1
                temp=nums[currIndex]
                nums[currIndex]=nums[swapIndex]
                nums[swapIndex]=temp
                break
            
            prevIndex=currIndex
            currIndex-=1
        
        def bubbleSort(st,en):
            for i in range(st,en+1):
                flag=True
                for j in range(st,en):
                    if comp(nums[j],nums[j+1]):
                        flag=False
                        temp=nums[j]
                        nums[j]=nums[j+1]
                        nums[j+1]=temp
                
                if flag:
                    break
        
        def comp(a,b):
            return a>b
        
        bubbleSort(currIndex+1,len(nums)-1)

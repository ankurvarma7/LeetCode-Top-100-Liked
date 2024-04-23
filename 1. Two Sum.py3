class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valueToIndex={}
        for i in range(len(nums)):
            if target-nums[i] in valueToIndex:
                return [valueToIndex[target-nums[i]],i]
            
            valueToIndex[nums[i]]=i

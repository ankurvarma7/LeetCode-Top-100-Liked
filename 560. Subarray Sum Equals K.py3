class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq=collections.defaultdict(int)

        sum=0
        res=0

        for num in nums:
            sum+=num
            if sum==k:
                res+=1
            
            if sum-k in freq:
                res+=freq[sum-k]
            
            freq[sum]+=1
        
        return res

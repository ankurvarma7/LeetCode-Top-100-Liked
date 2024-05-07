class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        curr=[]

        def solve(index,target):
            if target==0:
                res.append(curr.copy())
                return

            if index>=len(candidates):
                return
            
            if candidates[index]<=target:
                curr.append(candidates[index])
                solve(index,target-candidates[index])
                curr.pop()
            
            solve(index+1,target)
        
        solve(0,target)
        return res

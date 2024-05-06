class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp={}

        def solve(index,amount):
            if amount==0:
                return 0
            
            if index>=len(coins):
                return 100000
            
            if (index,amount) in dp:
                return dp[(index,amount)]
            

            dp[(index,amount)]=solve(index+1,amount)

            if coins[index]<=amount:
                dp[(index,amount)]=min(dp[(index,amount)],1+solve(index,amount-coins[index]))
            
            return dp[(index,amount)]
        
        res=solve(0,amount)

        return -1 if res==100000 else res

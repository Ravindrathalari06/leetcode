class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp=[amount+1]*(amount+1)
        # dp[0]=0
        # for i in range(1,amount+1):
        #     for coin in coins:
        #         if i>=coin:
        #             dp[i]=min(dp[i],dp[i-coin]+1)
        # if dp[amount]>amount:
        #     return -1
        # return dp[amount]
        memo={}
        
        def solve(amount):
            if amount==0:
                return 0
            if amount<0:
                return float('inf')
            if amount in memo:
                return memo[amount]
            best=float('inf')
            
            for coin in coins:
                res=solve(amount-coin)
                if res!=best:
                    best=min(best,res+1)
            memo[amount]=best
            return best
        result=solve(amount)
        return result if result!=float('inf') else -1
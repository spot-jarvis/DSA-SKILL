class Solution:
    def maximumProfit(self, prices):
        # code here
        mini = prices[0]
        res = 0
        for i in range(1,len(prices)):
            mini = min(mini,prices[i])
            
            res = max(res,prices[i] - mini)
        return res

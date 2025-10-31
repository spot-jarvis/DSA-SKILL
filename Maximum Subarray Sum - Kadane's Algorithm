class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        n = len(arr)
        res = arr[0]
        presum = arr[0]
        
        for i in range(1,n):
            presum +=  arr[i]
            if presum < arr[i]:
                presum = arr[i]
            res = max(res,presum)
        return res
# better way in least code 
#instead of looping that we can use these 
for i in range(1,n):
            presum = max(presum+arr[i],arr[i])
            res = max(presum ,res)
        return res

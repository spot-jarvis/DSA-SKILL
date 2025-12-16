class Solution:
    def maxCircularSum(self, arr):
        # code here
        currmin = 0
        currmax = 0
        maximum = arr[0]
        minimum = arr[0]
        totalSum = arr[0]
        n = len(arr)
        
        for i in range(1,n):
            #maximum using  kdanes
            currmax = max(currmax+arr[i],arr[i])
            maximum = max(currmax,maximum)
            
            #minimum using kdanes
            currmin = min(currmin+arr[i],arr[i])
            minimum = min(currmin,minimum)
            
            totalSum  +=arr[i]
            
        circularSum = totalSum - minimum 
        return max(circularSum , maximum )
            
# same way 
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        GlobalMax , GlobalMin = nums[0],nums[0]
        currMin = currMax = 0
        TotalSum = 0
        for num in nums:
            currMin = min(num,currMin+num)
            currMax = max(num,currMax+num)
            TotalSum += num
            GlobalMax = max(GlobalMax,currMax)
            GlobalMin = min(GlobalMin,currMin)
        return max(GlobalMax,TotalSum - GlobalMin) if GlobalMax > 0 else GlobalMax
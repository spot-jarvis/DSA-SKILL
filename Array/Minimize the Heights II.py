class Solution:
    def getMinDiff(self, arr, k):
        # code here
        n = len(arr)
        arr.sort()
        ans = arr[-1] - arr[0]
        small = arr[0]+k
        big = arr[-1]-k
        for i in range(1,n):
            if arr[i] -k < 0:
                continue
            curr_min = min(small,arr[i]-k)
            curr_max = max(big,arr[i-1]+k)
            ans = min(ans,curr_max-curr_min)
        return ans
        

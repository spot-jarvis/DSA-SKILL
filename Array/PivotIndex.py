#Brute force approach 

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            leftSum,rightSum = 0,0
            for l in range(i):
                leftSum += nums[l]
            for j in range(i+1,n):
                rightSum += nums[j]

            if rightSum == leftSum :
                return i
        return -1 
    
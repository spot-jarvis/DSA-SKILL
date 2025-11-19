class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n-2
        #finding the pivot value 
        while i >=0 and nums[i] >= nums[i+1]:
            i-=1
        if i < 0:
            return nums.reverse()
        j = n-1
        #finding the next successor
        while nums[j] <= nums[i]:
            j-=1
        nums[i],nums[j] = nums[j],nums[i]
#we cant reverse like the c so we do these manually
        left = i+1
        right = n-1
        while left < right:
            nums[left],nums[right] = nums[right],nums[left]
            left+=1
            right-=1
         
        

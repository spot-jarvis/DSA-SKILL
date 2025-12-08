class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                break
        for j in range(i+1,n):
            if nums[j] != 0:
                nums[j],nums[i] = nums[i],nums[j]
                i+=1
        return nums
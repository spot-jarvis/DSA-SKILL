class Solution:
    def QuickSort(self,nums:List[int], left: int, right: int):
        if left >= right:
            return 
        pivot = nums[right]
        low = left 
        for i in range(left,right):
            if nums[i] < pivot:
                nums[low],nums[i] = nums[i],nums[low]
                low+=1
        nums[low],nums[right] = nums[right],nums[low]

        self.QuickSort(nums,left,low-1)
        self.QuickSort(nums,low+1,right)



    def sortArray(self, nums: List[int]) -> List[int]:
        left ,right = 0,len(nums)-1
        self.QuickSort(nums,left,right)
        return nums
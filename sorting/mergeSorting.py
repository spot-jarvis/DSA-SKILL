class Solution:
    def mergeSort(self,nums: List[int], start: int, end: int):
        if start >= end :
            return nums

        mid = (start + end)//2
        self.mergeSort(nums, start, mid)
        self.mergeSort(nums, mid+1, end)
        self.merge(nums, start, mid, end)

        return nums

    def merge(self, nums: List[int], start: int, mid: int, end: int):
        Left = nums[start:mid+1]
        right = nums[mid+1:end+1]
        i,j,k = 0,0,start

        while i < len(Left) and j < len(right):
            if Left[i] <= right[j]:
                nums[k] = Left[i]
                i+=1
            else:
                nums[k] = right[j]
                j+=1
            k += 1

        while i < len(Left):
            nums[k] = Left[i]
            i+=1
            k+=1
        while j < len(right):
            nums[k] = right[j]
            j +=1
            k +=1




    def sortArray(self, nums: List[int]) -> List[int]:
        left , right = 0,len(nums)-1
        self.mergeSort(nums, left, right)

        return nums
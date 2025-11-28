class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele = count = 0
        n = len(nums)
        for i in range(n):
            if count == 0:
                count=1
                ele = nums[i]
            elif nums[i]  == ele:
                count += 1
            else:
                count -=1
        count = 0
        for i in range(n):
            if nums[i] == ele:
                count +=1
            
        if count > n//2:
            return ele
        return -1

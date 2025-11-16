# 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = []
        for i in range(0,n-1):
            if i > 0 and  nums[i-1] == nums[i]:
                continue
            left = i+1
            right = n-1
            while left < right :
                valsum = nums[left] + nums[right] + nums[i]
                if valsum == 0:
                    result.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -=1
                    while left < right and nums[left] == nums[left-1]:
                        left +=1
                    while left < right  and nums[right] == nums[right+1]:
                        right -=1
                elif valsum > 0:
                    right -=1
                else :
                    left += 1
        return result

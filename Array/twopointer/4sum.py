class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n-1):
            if i >0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,n-1):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                
                left , right = j+1,n-1
                while left < right :
                    currsum = nums[i]+nums[j]+nums[left]+nums[right]
                    if currsum == target:
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        left += 1
                        right -=1

                        while left < right and nums[left-1] == nums[left]:
                            left +=1
                        while left < right and nums[right] == nums[right+1]:
                            right -=1
                    elif currsum > target:
                        right -=1
                    else :
                        left +=1
        return res 
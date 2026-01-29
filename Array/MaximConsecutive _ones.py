class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxim = 0
        count = 0

        for num in nums:
            if num == 1:
                count +=1
                maxim = max(maxim,count)
            else:
                count = 0
        
        return maxim
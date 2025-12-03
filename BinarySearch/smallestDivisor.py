class Solution:

    def is_divisible(self,nums:list[int],k:int,threshold : int) -> bool:
        divisor = 0
        for num in nums:
            divisor += (num + k-1 )//k
            if divisor > threshold:
                return False
        return True

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left ,right = 1,max(nums)
        result = 0
        while left <= right:
            mid = (left + right)//2
            if self.is_divisible(nums,mid,threshold):
                result = mid
                right = mid -1
            else:
                left = mid+1
        return result

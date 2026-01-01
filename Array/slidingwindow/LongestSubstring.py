class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        totalSum = left = 0
        res = float('inf')

        for right in range(len(nums)):
            totalSum += nums[right]
            while totalSum >= target:
                res = min(right - left +1, res)
                totalSum -= nums[left]
                left += 1
        return 0 if res == float('inf') else res
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 0
        numbers = set(nums)
        for num in numbers :
            if num-1 not in numbers: # for finding the starting number 
                length = 1
                y = num +1
                while y in numbers:
                    length += 1
                    y+=1
                res = max(res,length)
        return res
#we can use the sort method but its nlogn time complexity //

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ele1 = ele2 = count1 = count2 = 0
        n = len(nums)
        result = []
        for num in nums:
            if count1 == 0 and num != ele1:
                count1 = 1
                ele1 = num
            elif count2 == 0 and num!= ele2:
                count2 = 1
                ele2 = num
            elif num == ele1:
                count1+=1
            elif num == ele2:
                count2+=1
            else:
                count1 -= 1
                count2 -= 1

        count1 = count2 = 0
        for num in nums:
            if num == ele1:
                count1 +=1
            elif num == ele2:
                count2 +=1
        if count1 > n//3 :
            result.append(ele1)
        if count2 > n//3:
            result.append(ele2)
        return result
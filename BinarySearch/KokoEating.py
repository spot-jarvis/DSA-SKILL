class Solution:


    def can_eat(self,piles : list[int],k:int,h:int) -> bool:
        hours = 0
        for pile in piles:
            hours += (pile + k-1)//k
        if hours > h :
            return False
        return hours <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left ,right = 1,max(piles)
        result = 0
        while left <= right:
            mid = (left + right)//2
            if self.can_eat(piles,mid,h):
                result = mid
                right = mid-1
            else:
                left = mid+1
        return result 
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay) :
            return -1

        def can_make(day : int) -> bool:
            consecutive = 0
            bouqet = 0
            for b in bloomDay:
                if b <= day:
                    consecutive +=1
                    if consecutive == k:
                        bouqet += 1
                        consecutive = 0
                        if bouqet >= m:
                            return True
                else:
                    consecutive = 0
            return bouqet >= m

        left ,right = min(bloomDay),max(bloomDay)
        ans = -1
        while left <= right:
            mid = (left + right)//2
            if can_make(mid):
                ans = mid
                right = mid-1
            else:
                left = mid+1
        return ans

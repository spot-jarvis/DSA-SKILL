class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count,expected = 0,1
        n = len(arr)
        i= 0
        while count < k:
            if i < n and arr[i] == expected :
                i+=1
            else:
                count +=1
                expected += 1

        return expected -1
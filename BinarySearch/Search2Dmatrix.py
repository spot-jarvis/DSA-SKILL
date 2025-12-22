class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left,right  = 0, (m*n)-1

        while left <= right:
            mid = (left+right)//2
            # mid //n representing the row and %n representing the column 
            ele = matrix[mid//n][mid%n]
            if ele == target:
                return True
            if ele < target:
                left = mid +1
            else :
                right = mid -1
        return False
        
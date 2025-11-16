class Solution:
    def missingNumber(self, arr):
        # code here
        n = len(arr)
        
        for i in range(n):
            if arr[i] <= 0 or arr[i] > n:
                arr[i] = n+1
                
        for i in range(n):
            x = abs(arr[i])
            if 1 <= x <= n:
                arr[x-1] = -abs(arr[x-1])
                
        for i in range(n):
            if arr[i] > 0:
                return i+1
        
        return n+1


#there is an another way also using a set and check if all the elements are there if not return i+1  otherwise return n+1 but it take O(n) space and time 

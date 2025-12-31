#using prefix sum

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        prefix_sum = [0] * (len(arr)+1)
        for i in range(len(arr)):
            prefix_sum[i+1] = prefix_sum[i] + arr[i]

        result = left = 0
        for right in range(k-1,len(arr)):
            sum_ = prefix_sum[right + 1] - prefix_sum[left]
            if sum_/k >= threshold:
                result += 1
            left += 1
        return result
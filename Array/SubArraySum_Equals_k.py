class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mpp = {0:1}
        presum = 0
        count = 0

        for num in nums:
            presum += num
            remove = presum -k
            if remove in mpp:
                count += mpp[remove]
            mpp[presum] = mpp.get(presum,0)+1
        return count
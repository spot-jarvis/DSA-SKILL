class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        result = []
        for num in nums:
            freq[num] = freq.get(num,0)+1
    # here we change the dictionary to list like [(key,value),(key,value)]
        pairs = list(freq.items())
# we sort the pairs based on the value .lambda is using for geting the value
        pairs.sort(key = lambda x:x[1],reverse = True)
        for i in range(k):
            result.append(pairs[i][0])
        return result 


# we can use bucket sorting based on the freq its O(n) 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num,0)+1
        
        for num,value in count.items():
            freq[value].append(num)
        
        res = []
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) ==k:
                    return res
        return res

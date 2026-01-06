#backtracking 
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return 
            if total > target or i >= len(candidates):
                return 

            curr.append(candidates[i])
            dfs(i,curr, total + candidates[i])
            curr.pop()
            dfs(i+1, curr, total)
        
        dfs(0,[],0)
        return res
    

#optimal way by using sorting we can skip the unwanted iteration

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return 
            
            for j in range(i,len(nums)):
                if nums[j] + total > target:
                    return 
                curr.append(nums[j])
                dfs(j,curr,total+nums[j])
                curr.pop()

        dfs(0,[],0)
        return res
        
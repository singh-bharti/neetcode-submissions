class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        targetSubset = []
        nums.sort()
        subset = []
        def dfs(i, subset, sum):
            if sum == target:
                targetSubset.append(subset.copy())
                return;
            for j in range(i, len(nums)):
                if sum + nums[j] > target:
                    return
                subset.append(nums[j])
                dfs(j, subset, sum + nums[j])
                subset.pop()
           
        dfs(0, subset, 0)
        return targetSubset
            
        
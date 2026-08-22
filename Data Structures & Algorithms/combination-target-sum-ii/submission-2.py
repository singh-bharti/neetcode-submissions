class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        targetSubset = [] #[1,2,3,4,5]
        candidates.sort()
        subset = []
        def dfs(i, subset, sum): #(0, [], 0)
            if sum == target: # 0 == 7 -> false
                targetSubset.append(subset.copy())
                return;
            for j in range(i, len(candidates)):#j =i =0
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if sum + candidates[j]  > target: # 0 + 1, 3
                    break;
                subset.append(candidates[j]) #[1,2, 3]
                dfs(j+1, subset, sum + candidates[j]) 
                subset.pop()
           
        dfs(0, subset, 0) # (0, [], 0)
        return targetSubset

        
        
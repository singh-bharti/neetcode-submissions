class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        def dfs(i):
            if i > len(nums) - 1:
                res.append(cur.copy())
                return
            #make a choice
            cur.append(nums[i])
            #backtrack
            dfs(i + 1)
            #remove that choice
            cur.pop()
            #backtrack
            dfs(i + 1)
        dfs(0)

        return res



        
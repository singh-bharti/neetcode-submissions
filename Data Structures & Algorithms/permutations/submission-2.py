class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)
        def dfs(subset, used):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                subset.append(nums[i])
                used[i] = True

                dfs(subset, used)

                subset.pop()
                used[i] = False
        dfs([], used)
        return res





        
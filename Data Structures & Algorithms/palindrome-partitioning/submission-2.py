class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []
        def dfs(i):
            if i == len(s):
                res.append(subset.copy())
                return
            
            for j in range(i, len(s)):
                cur = s[i:j+1]

                if isPallindrome(cur):
                    subset.append(cur)
                    dfs(j+1)
                    subset.pop()

        def isPallindrome(curStr):
            return curStr == curStr[::-1]
        
        dfs(0)

        return res



            
        
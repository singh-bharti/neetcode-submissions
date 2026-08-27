class Solution:
    def isHappy(self, n: int) -> bool:

        if n <= 0: 
            return False
        seen = []
        def dfs(n):
            sum = 0
            for digit in str(n):
                sum += int(digit) ** 2
            if sum == 1:
                return True
            if sum in seen:
                return False
            seen.append(sum)
            return dfs(sum)      
        return dfs(n)

        
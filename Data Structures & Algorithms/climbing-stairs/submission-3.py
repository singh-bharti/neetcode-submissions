class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        prev_i2 = 2
        prev_i1 = 1
        for i in range(3, n+1):
            cur = prev_i1 + prev_i2 
            prev_i1 = prev_i2
            prev_i2 = cur
        return prev_i2
        
        
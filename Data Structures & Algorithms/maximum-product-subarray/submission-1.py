class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currentMax = nums[0]
        currentMin = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            x = nums[i]
            newMax = max(x, x * currentMax, x * currentMin)
            newMin = min(x, x * currentMax, x * currentMin)
            
            currentMax = newMax
            currentMin = newMin

            result = max(result, currentMax)
        return result


        
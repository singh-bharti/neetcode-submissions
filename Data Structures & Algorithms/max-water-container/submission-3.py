class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1;
        maxCapacity = 0
        while l < r:
            amount =( r - l) * min(heights[r], heights[l]);
            maxCapacity = max(amount, maxCapacity);
            if heights[r] >= heights[l]: l += 1
            else:  r -= 1
        return maxCapacity
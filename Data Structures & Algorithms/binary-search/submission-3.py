class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l= 0;
        r= len(nums);
        
        while l < r:
            m = (l+(r-1))//2;
            if nums[m] > target:
                r = m;
            elif nums[m] < target:
                l = m + 1;
            else:
                return m;
        return -1;

        
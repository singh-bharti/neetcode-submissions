class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums: number[]): number[][] {
        nums.sort((a, b) => a - b);
        if (nums.length < 3) return [];
        let res = [];
        const n = nums.length;

        for (let i = 0; i < n - 2; i++) {
            if (i > 0 && nums[i] === nums[i -1]) continue;
            let j = i + 1;
            let k = n - 1;
            while (j < k) {
                let sum = nums[i] + nums[j] + nums[k];
                if (sum === 0) {
                    res.push([nums[i], nums[j], nums[k]]);
                    while (j < k && nums[j] === nums[j + 1]) {
                        j++;
                    }
                    while (j < k && nums[k] === nums[k - 1]) {
                        k--;
                    }
                    j++;
                    k--;
                } else if (sum > 0) {
                    k--;
                } else {
                    j++;
                }
            }
        }
        return res;
    }
}



    


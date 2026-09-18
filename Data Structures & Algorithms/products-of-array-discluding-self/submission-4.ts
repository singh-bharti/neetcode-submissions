class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums: number[]): number[] {
        const n: number = nums.length;
        const prefix: number[] = new Array(n);
        const postfix: number[] = new Array(n);
        const result: number[] = new Array(n);
        prefix[0] = 1
        postfix[n - 1] = 1

        for (let i = 1; i < n; i++) {
            prefix[i] = nums[i-1] * prefix[i-1]
        }
        for (let i = n-2; i >= 0; i--) {
            postfix[i] = nums[i+1] * postfix[i+1]
        }
        for (let i = 0; i < n; i++) {
            result[i] = prefix[i] * postfix[i]
        }
        return result;
    }
}

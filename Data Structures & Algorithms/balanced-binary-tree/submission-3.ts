/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {boolean}
     */
    isBalanced(root: TreeNode | null): boolean {
        if (!root) return true;
        let diff = this.helper(root) !== -1
        return diff;
        
    }

    helper(root) {
        if (!root) return 0;

        const leftDepth = this.helper(root.left);

        if (leftDepth === -1) return -1;

        const rightDepth = this.helper(root.right);

        if (rightDepth === -1) return -1;

        if (Math.abs(rightDepth - leftDepth) > 1) {
            return -1;
        }

        return 1 + Math.max(leftDepth, rightDepth);
    }
}

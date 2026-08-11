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
     * @return {number[][]}
     */
    levelOrder(root: TreeNode | null): number[][] {
        if (!root) return [];
        const res = [];
        const queue = [root];
        let front = 0;
        while (front < queue.length) {
            let level = [];
            let levelSize = queue.length - front;
            for (let i = 0; i < levelSize; i++) {
                //pushing current value in level
                let node = queue[front++];
                level.push(node.val);

                if (node.left) {
                    queue.push(node.left);
                }
                if (node.right) {
                    queue.push(node.right);
                }
            }
            res.push(level);
        }
        return res;
    }
}

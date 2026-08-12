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
     * @return {number[]}
     */
    rightSideView(root: TreeNode | null): number[] {
        if (!root) return [];
        const res = [];
        const queue = [root];
        let front = 0;
        while (front < queue.length) {
            let levelLen = queue.length - front;
            for (let i = 0; i < levelLen; i++) {
                let node = queue[front++];
                if (i === (levelLen - 1)) {
                    res.push(node.val)
                }
                if (node.left) {
                    queue.push(node.left) // [1,2]
                } 
                if (node.right) {
                    queue.push(node.right) //[1,2,3]
                }
            }
        }
        return res;
    }
}
 












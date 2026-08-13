# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def validate(node, min, max):
            if not node:
                return True
            if not (min < node.val < max):
                return False
            else:
                return (validate(node.left, min, node.val) and validate(node.right, node.val, max))
        return validate(root, float("-inf"), float("inf"))

    
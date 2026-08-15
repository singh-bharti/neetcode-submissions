# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if (not preorder) or (not inorder):
            return None

        inoderMap = {value: i for i, value in enumerate(inorder)}
        self.preorderIndex = 0
        def dfs(left, right):
            if left > right:
                return None
            rootVal = preorder[self.preorderIndex]
            self.preorderIndex += 1
            root = TreeNode(rootVal)
            mid = inoderMap[rootVal]
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid+1, right)
            return root

        return dfs(0, len(inorder)-1)
        
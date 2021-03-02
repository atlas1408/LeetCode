# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        maxSum = float('-inf')
        def rec(node):
            nonlocal maxSum
            if not node:
                return 0
            left = rec(node.left)
            right = rec(node.right)
            maxSum = max(maxSum, node.val, left + node.val, right + node.val, left + node.val + right)
            return max(node.val, node.val+left, node.val+right)
        rec(root)
        return maxSum
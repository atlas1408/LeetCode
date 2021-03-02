# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        sol = -1
        index = 0
        def rec(node):
            nonlocal sol, index
            if not node:
                return
            rec(node.left)
            index+=1
            if index == k:
                sol = node.val
                return 
            rec(node.right)
        rec(root)
        return sol